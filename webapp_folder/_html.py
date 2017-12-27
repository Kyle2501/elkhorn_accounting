# -*- coding: latin-1 -*-
# - HTML Page Code



hi_test = 'hi hi hi'



login_page = '''

please login

'''

intro_page = '''

welcome to intro

'''


front_page = '''<style>


.week_wrap { position: relative; padding-bottom: 45px; }
.week_data { background-color: #E8EAF6; padding: 10px; padding-bottom: 15px; padding-top: 15px; }

.day_wrap { border: 1px solid #ccc; width: 24%; display: inline-block; margin-left: .5%; background-color: #fff; }
.day_data { outline: 1px solid #ccc; padding-bottom: 35px; background-color: #fff; }
.day_wrap:hover .day_data { outline: 1px dashed #ccc; }
.day_header { text-align: right; margin-left: 15px; margin-right: 15px; padding-right: 10px; padding-top: 5px; padding-bottom: 2px; border-bottom: 1px solid #eee; letter-spacing: .07em; font-family: 'Monda', sans-serif; }
.day_name { font-size: 14px; color: #839496; float: left; padding-left: 15px; }

.day_wrap:hover .day_header { border-bottom: 1px solid #333; }

.day_times { margin-left: 10px; margin-top: 40px; font-family: 'Monda', sans-serif; }
.day_times ul { padding: 0; margin: 0; }
.day_times ul li { list-style: none; margin-bottom: 9px; outlite: 1px solid #eee; font-size: 12px; }
.day_times ul li:hover { cursor: pointer; border-bottom: 1px solid: #eee; }
.time_dot { width: 7px; height: 7px; background-color: #DCEDC8; border-radius: 50%; display: inline-block; margin-right: 10px; }

.day_times ul li:hover .time_dot { background-color: #EF5350; }

.time_hour { display: inline-block; float: right; margin-right: 10px; color: #93a1a1; font-size: 11px; }

.day_times ul li:hover .time_hour { color: #586e75; }
.time_slot div { display: inline-block; }

/*.current_day{ border-bottom: 1px solid #CE93D8; }*/

.day_bottom { display: inline-block; font-size: 11px; letter-spacing: 0.2em; padding-top: 5px; float: right; padding-right: 10px; font-family: 'Raleway', sans-serif; margin-bottom: 10px; }

.day_times_on { display: block; }
.day_times_off { display: none; }

.show_time_button {  border: 1px solid #aaa; padding: 5px; text-align: center; cursor: pointer; width: 75px; margin: 10px; font-size: 10px; margin-top: 45px; font-family: 'Playfair Display', serif; letter-spacing: 0.08em; position: absolute; right: 25px; }

</style>
<br />
<p>welcome to front page</p>

<div class="agenda_wrap">

<div class="week_wrap">
  <div class="week_data">

  <div class="day_wrap" ng-repeat="day in week_days | startFrom: day_of_week - 2 | limitTo:4" ng-class="{current_day: day.day_number == weekday}"
  ng-if="day.day_number > weekday - 2">
  <div class="day_data">

    <div class="day_header">
      <span class="day_name">[!day.day_name!]</span>
      <span ng-if="day.day_number < weekday" style="color:#ccc;">&#5788;</span>
      <span ng-if="day.day_number == weekday">&#5787;</span>
      <span ng-if="day.day_number > weekday" style="color:#ccc;">&#5787;</span>
    </div><!-- . day_header - -->


  <div class="day_bottom">
    <span ng-if="day.day_number == weekday">
    [!month_day!] &nbsp; Today</span>
    <span ng-if="day.day_number == weekday + 1">Tomorrow</span>
    <span ng-if="day.day_number == weekday - 1">Yesterday</span>
    <span ng-if="day.day_number == weekday + 2">In Two Days</span>
  </div>
  
  <div class="day_times day_times_[!show_times_4day_view!]"><ul>
      <li class="time_slot" ng-repeat="hour in day_hours">
        <div class="time_dot"></div>
        <div class="hour_event" ng-repeat="item in agenda_list">
          <span ng-click="selectStudent(item)" ng-if="item.agenda_time == hour && item.agenda_day == day.day_number">
            [!item.agenda_name!]</span>
        </div>
        <div class="time_hour">[!hour!]</div>
      </li><!-- . time_slot - -->

    </ul></div><!-- .day_times - -->
  </div><!-- . day_data - -->
  
</div><!-- . day_wrap - -->

</div><!-- . week_data - -->



<div class="show_time_button" ng-click="show_times_4day_view='off'" ng-show="show_times_4day_view == 'on'">Close Times</div>
<div class="show_time_button" ng-click="show_times_4day_view='on'" ng-show="show_times_4day_view == 'off'">Show Times</div>

</div><!-- . week_wrap - -->



<style>

.month_wrap { width: 410px; margin-top: 50px; display: inline-block; border-right: 1px solid #ccc; }
.month_day_wrap { display: inline-block; margin: 5px; width: 45px; padding-top: 10px; height: 30px; text-align: center; cursor: pointer; }
.month_day_wrap:hover { outline: 1px solid #ddd; }
.month_first_day { border-bottom: 1px solid #bbb; }
.past_days { color: #bbb; }
.current_day { outline: 1px solid #268bd2; }

.month_day_detail { display: inline-block; vertical-align: top; margin-top: 50px; margin-left: 25px;  }

.month_day_number { font-size: 32px; margin: 15px; border-bottom: 1px solid #aaa; width: 50px; text-align: center; }

</style>

<div class="month_wrap">
  
  <div class="month_day_wrap" ng-repeat="item in month_days | startFrom: (month_day - day_of_week - 1)" ng-class="{current_day: item == month_day }" ng-click="showDetail(item)">
    <span  ng-class="{past_days: item < month_day}">[!item!]</span>
  </div>

  <div class="month_day_wrap" ng-repeat="item in month_days | limitTo: future_months_1" ng-class="{month_first_day: item < 2}">
    <span>[!item!]</span>
  </div>




</div><!-- .month_wrap - -->




</div><!-- . agenda_wrap - -->
'''

main_page = '''

welcome to main page

'''

## -

user_page = '''

welcome to user page

'''

account_page = '''

welcome to account page

'''

