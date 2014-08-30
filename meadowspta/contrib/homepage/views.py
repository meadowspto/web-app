from django.template import RequestContext, Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from meadowspta.contrib.news.models import News
from meadowspta.contrib.system.models import sysvar

def view(request):
    board = [
        {
            'title': 'President',
            'name': 'Leola Meiners',
        },
        {
            'title': 'VP of Fundraising',
            'name': 'Vivian Chu',
        },
        {
            'title': 'VP of Communications',
            'name': 'Lia Hanson',
        },
        {
            'title': 'VP of Membership',
            'name': 'Chris Mezzetta',
        },
        {
            'title': 'Treasurer/Financial Officer',
            'name': 'Steven Cashiola',
        },
        {
            'title': 'Financial Auditor',
            'name': 'Doris Lim',
        },
        {
            'title': 'Secretary',
            'name': 'Heather Mezzetta',
        },
        {
            'title': 'Parlimentarian',
            'name': 'Craig Yonemura',
        },
        {
            'title': 'Historian',
            'name': 'Jill Hinck',
        },
    ]

    news = News.objects.all().exclude(id=int(sysvar['news_featured_post'])).order_by('-publish_date')[:4]
    featured_news_post = News.objects.get(id=int(sysvar['news_featured_post']))

    payload = dict(
        board=board,
        news=news,
        featured_news_post=featured_news_post
    )

    return render_to_response('homepage/view.html', payload, context_instance=RequestContext(request))
