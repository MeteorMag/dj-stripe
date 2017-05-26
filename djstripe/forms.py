# -*- coding: utf-8 -*-
"""
.. module:: djstripe.forms
   :synopsis: dj-stripe Forms.

.. moduleauthor:: Daniel Greenfeld (@pydanny)

"""

from django import forms
from .models import return_plan_choices


class PlanForm(forms.Form):

    plan = forms.ChoiceField(choices=return_plan_choices())

    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        # Make form fully dynamic.
        self.fields['plan'] = forms.ChoiceField(choices=return_plan_choices())
        super(PlanForm, self).full_clean()


class CancelSubscriptionForm(forms.Form):
    pass
