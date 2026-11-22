from django.shortcuts import render
from django.db.models import Count
from django.db.models import F
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .models import Vote, Poll


STATUS_MAP = {
    "active": Poll.PollStatus.ACTIVE,
    "finished": Poll.PollStatus.FINISHED,
}


def poll_list(request):
    search_query = request.GET.get("q", "").strip()
    status_filter = request.GET.get("status", "all")

    polls = Poll.objects.all().order_by("-created_at")

    if search_query:
        polls = polls.filter(question__icontains=search_query)

    status_code = STATUS_MAP.get(status_filter)
    if status_code:
        polls = polls.filter(status=status_code)

    paginator = Paginator(polls, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "votes/poll_list.html",
        {
            "page_obj": page_obj,
            "paginator": paginator,
            "is_paginated": page_obj.has_other_pages(),
            "search_query": search_query,
            "current_status": status_filter,
        },
    )


def poll_detail(request, poll_id):
    poll = get_object_or_404(
        Poll,
        pk=poll_id
    )

    choices_data = poll.choices.all().annotate(votes_count=Count('votes'))

    return render(
        request,
        "votes/poll_detail.html",
        {
            "poll": poll,
            "choices_data": choices_data,
        },
        status=200,
    )


def statistics(request):

    total_polls = Poll.objects.count()
    total_votes = Vote.objects.count()
    status_polls = (
            Poll.objects
            .values('status')
            .annotate(total=Count('id'))
            .order_by('status')
        )

    stats = (
        Poll.objects.annotate(votes_count=Count("votes"))
        .values("question", "votes_count")
        .order_by("-votes_count")
    )

    recent_votes = (
        Vote.objects
        .annotate(
            username=F("user__username"),
            question=F("poll__question"),
            title=F("choice__title"),
        )
        .values("username", "question", "title", "created_at")
        .order_by("-created_at")[:5]
    )

    return render(request, "votes/statistics.html", {
        "total_polls": total_polls,
        "total_votes": total_votes,
        'active': status_polls[0],
        'finish': status_polls[1],
        "stats": stats,
        "recent_votes": recent_votes,
        }
    )


def page_not_found(request, exception):
    return render(request, "pages/404.html", status=404)
