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


class CancelSubscriptionForm(forms.Form):
    pass
