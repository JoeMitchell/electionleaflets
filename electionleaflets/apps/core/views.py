from django.template  import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.sites.models import Site


def home(request):
    from constituencies.forms import ConstituencyLookupForm

    form = ConstituencyLookupForm(request.POST or None)

    return render_to_response('core/home.html',
        {'form': form,},
        context_instance=RequestContext(request) )


def report_abuse(request, id):
    from core.forms import ReportAbuseForm
    from leaflets.models import Leaflet

    leaflet = get_object_or_404( Leaflet, id=id )

    form = ReportAbuseForm( request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            domain = Site.objects.get_current().domain
            ctx = {
                'link': 'http://%s%s' % (domain, reverse('leaflet', kwargs={'object_id':leaflet.id}),),
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'details': form.cleaned_data['details'],
            }

            subject, from_email, to = settings.EMAIL_SUBJECT, settings.EMAIL_FROM, settings.EMAIL_RECIPIENT

            text_content = render_to_string('email/abuse_report.txt', ctx)
            html_content = render_to_string('email/abuse_report.html', ctx)

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return HttpResponseRedirect( reverse('report_abuse_sent', kwargs={'id': id}))

    return render_to_response('core/report_abuse.html', {
        'leaflet': leaflet, 'form': form },
        context_instance=RequestContext(request) )
