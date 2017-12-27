#!/usr/bin/env python
# -*- coding: latin-1 -*-

Site = 'Accounting . Elkhorn.io'

Timezone = 'Pacific/Honolulu'


  # - System
import os
import cgi
import urllib
import wsgiref.handlers
import datetime
import time
import calendar as cal
import json, ast
import sys,imp
  # - Appengine
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
from urlparse import urlparse
  # -
from google.appengine.ext import ndb
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp.util import run_wsgi_app
from pytz.gae import pytz

import _html as _html




#----------------------------------------------#
#        Completed Data Stucture               #
#----------------------------------------------#
class Agenda_db(ndb.Model):
    data_id = ndb.StringProperty()
#
    user_id = ndb.StringProperty()
    user_email = ndb.StringProperty()
#
    item_id = ndb.StringProperty()
    item_name = ndb.StringProperty()
    item_kind = ndb.StringProperty()
#
    item_status = ndb.StringProperty()
    status_date = ndb.StringProperty()

    @classmethod
    def _get_my_status(self):
      client_email = users.get_current_user().email()
      q = People_db.query(People_db.user_email == client_email)
      db_data = []
      for item in q.iter():
        db_data.append(item.to_dict(exclude=['user_id','user_email']))
      return json.dumps(db_data)


class updatePeople_db(webapp2.RequestHandler):
  def post(self):
    page_address = self.request.uri
    base = os.path.basename(page_address)
    
    user = users.get_current_user()
    if user:
        item_id = self.request.get('item_id')
        client_email = user.email()
        key_name = item_id + '_' + client_email
        item = People_db.get_by_id(key_name)
        
        if not item:
            item = People_db(id=key_name)
        
        item.user_id = user.user_id()
        item.user_email = user.email()
        item.status_date = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")
        

        item.item_id = self.request.get('item_id')
        item.item_name = self.request.get('item_name')
        item.item_kind = self.request.get('item_kind')
        item.item_status = self.request.get('item_status')

        item.put()
        
    self.redirect('/my_info')



#----------------------------------------------#
#        Completed Data Stucture               #
#----------------------------------------------#
class People_db(ndb.Model):
    data_id = ndb.StringProperty()
#
    user_id = ndb.StringProperty()
    user_email = ndb.StringProperty()
#
    item_id = ndb.StringProperty()
    item_name = ndb.StringProperty()
    item_kind = ndb.StringProperty()
#
    item_status = ndb.StringProperty()
    status_date = ndb.StringProperty()

    @classmethod
    def _get_my_status(self):
      client_email = users.get_current_user().email()
      q = People_db.query(People_db.user_email == client_email)
      db_data = []
      for item in q.iter():
        db_data.append(item.to_dict(exclude=['user_id','user_email']))
      return json.dumps(db_data)


class updatePeople_db(webapp2.RequestHandler):
  def post(self):
    page_address = self.request.uri
    base = os.path.basename(page_address)
    
    user = users.get_current_user()
    if user:
        item_id = self.request.get('item_id')
        client_email = user.email()
        key_name = item_id + '_' + client_email
        item = People_db.get_by_id(key_name)
        
        if not item:
            item = People_db(id=key_name)
        
        item.user_id = user.user_id()
        item.user_email = user.email()
        item.status_date = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")
        

        item.item_id = self.request.get('item_id')
        item.item_name = self.request.get('item_name')
        item.item_kind = self.request.get('item_kind')
        item.item_status = self.request.get('item_status')

        item.put()
        
    self.redirect('/my_info')




#----------------------------------------------#
#        Completed Data Stucture               #
#----------------------------------------------#
class Progress_db(ndb.Model):
    data_id = ndb.StringProperty()
#
    user_id = ndb.StringProperty()
    user_email = ndb.StringProperty()
#
    item_id = ndb.StringProperty()
    item_name = ndb.StringProperty()
    item_kind = ndb.StringProperty()
#
    item_status = ndb.StringProperty()
    status_date = ndb.StringProperty()

    @classmethod
    def _get_my_status(self):
      client_email = users.get_current_user().email()
      q = People_db.query(People_db.user_email == client_email)
      db_data = []
      for item in q.iter():
        db_data.append(item.to_dict(exclude=['user_id','user_email']))
      return json.dumps(db_data)


class updateProgress_db(webapp2.RequestHandler):
  def post(self):
    page_address = self.request.uri
    base = os.path.basename(page_address)
    
    user = users.get_current_user()
    if user:
        item_id = self.request.get('item_id')
        client_email = user.email()
        key_name = item_id + '_' + client_email
        item = People_db.get_by_id(key_name)
        
        if not item:
            item = People_db(id=key_name)
        
        item.user_id = user.user_id()
        item.user_email = user.email()
        item.status_date = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")
        

        item.item_id = self.request.get('item_id')
        item.item_name = self.request.get('item_name')
        item.item_kind = self.request.get('item_kind')
        item.item_status = self.request.get('item_status')

        item.put()
        
    self.redirect('/my_info')






class publicSite(webapp2.RequestHandler):
    def get(self):
      # - URL Parse
        page_address = self.request.uri
        uri = urlparse(page_address)
        path = uri[2] # - uri.path
        layers = path.split('/')
        path_layer = layers[1]
        base = os.path.basename(page_address)
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.nickname()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
      # - app data
      
        html_file = 'main_layout.html'

        page_html = _html.front_page
        page_id = ''
        page_name = 'Front Page'
        nav_select = ''
        
        
      # -
        if path_layer == 'my_info':
            page_html = _html.user_page + _html.account_page
            page_id = 'my_info'
            page_name = 'My Info'
            nav_select = 'my_info'
            user_header = 'on'
            
        today_date = datetime.datetime.now(pytz.timezone(Timezone))
        weekday = datetime.date.isoweekday(today_date)
        week_number = today_date.strftime("%W")
      #
        month_number = today_date.strftime("%m")
        month_name = today_date.strftime("%B")
        month_day = today_date.strftime("%d")
        year_day = today_date.strftime("%j")
        year = today_date.strftime("%Y")


        day_of_the_month = int(month_day)
        day_of_week = int(weekday)
        days_left = 7 - day_of_week
        monday_number = day_of_the_month - day_of_week + 1
        sunday_number = day_of_the_month + days_left

        day_number = [1,2,3,4,5,6,7]
        day_name = ['Mon','Tues','Wed','Thurs','Fri','Satur','Sun']
        week_range = []
        for _ in range(int(monday_number), int(sunday_number)):
            week_range.append(_)


        week_day_keys = ['day_name','day_number','month_day']

        for value in range(4):
            test = {key: value for key in week_day_keys}


        calendar = cal.monthrange(int(year),int(month_number))
        future_months_1 = 0 # cal.monthrange(int(year),int(int(month_number) + 1))
        future_months_2 = 0 # cal.monthrange(int(year),int(int(month_number) + 2))
        future_months_3 = 0 # cal.monthrange(int(year),int(int(month_number) + 5))
        future_months_4 = 0 # cal.monthrange(int(year),int(int(month_number) + 5))
        future_months_5 = 0 # cal.monthrange(int(year),int(int(month_number) + 5))
        calendar2 = calendar
        days_month = calendar[1]
        calendar = days_month
        days_in_month = int(days_month)

        if sunday_number <= days_in_month:
            sunday = ''
            
        week_days = [
          {'day_number': 1,'day_name': 'Mon','month_day': ''},
          {'day_number': 2,'day_name': 'Tues','month_day': ''},
          {'day_number': 3,'day_name': 'Wed','month_day': ''},
          {'day_number': 4,'day_name': 'Thurs','month_day': ''},
          {'day_number': 5,'day_name': 'Fri','month_day': ''},
          {'day_number': 6,'day_name': 'Satur','month_day': ''},
          {'day_number': 7,'day_name': 'Sun','month_day': ''}
        ]


      # - template
        objects = {

            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
        
            'page_id': page_id,
            'page_name': page_name,
            'nav_select': nav_select,
        
            'page_html': page_html,


                    'today_date': today_date,
        'weekday': weekday,
        'week_number': week_number,
        'month_name': month_name,
        'month_day': month_day,
        'year_day': year_day,
        'year': year,

        'calendar': calendar,
        'days_left': days_left,
        'week_range': week_range,
        'week_days': week_days,
        'day_of_week': day_of_week,
        'days_month': days_month,
        
        
        
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html/%s' %html_file)
        self.response.out.write(template.render(path, objects))




app = webapp2.WSGIApplication([    # - Pages
    ('/', publicSite),
    
    ('/my_info', publicSite),
    ('/my_progress', publicSite),
    
    ('/add_people', updatePeople_db),
    
    ('/add_progress', updateProgress_db),
    
    
    ('/site_people', publicSite),
  

], debug=True)
