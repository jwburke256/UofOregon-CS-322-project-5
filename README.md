# UOCIS322 - Project 5 #
Continuation of the Brevet time calculator but now with MongoDB and docker-compose.

## Overview

A continuation of the brevet calculator now using MongoDB and docker-compose. Docker-compose makes it easier to create, manage and connect multiple container to create a single service comprised of different sub-services. For example this project now has both a web service that issues pages and jsons, as well as a new MongoDB service for storing and requesting brevit data. MongoDB is a Non Relational (NoSQL) database program that allows us to refactor our previous project to be more table drive. 


### ACP controle times

This project consists of a web application that is based on RUSA's online calculator. Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders). When using the webapp, you are presented with a grid in which to enter either your mile or distance markers. At the top there is a drop down for the overall brevit distance, as well as the starting date/time. Once a control has been typed into a submission field, the webapp will update and provide correspondiong opening and closing control times.

This webapp is based on and utilized the calculator found here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html).

### ACP Brevet Algorithm

In order to calculate the individual opening and closing brevet times, there is an algorithm that can be used along with a corresponding chart of maximum and minimum speeds. Essentially the algorithm takes a given control location, and the end brevet distance. From there the mathematical algorithm divides the given control distance by the minimum/maximum speed, with the integer portion of the result being the hours. For the minutes, you take the remainder and multiply by 60 then round. Finally one just has to take the new time and add it to the original start time to determine the corresponding brevits. There are additional edge cases to look out for which are accounted for such as having a control under 60km, having a start time early on end before any late arrivals begin, and having a control slightly over the final ending brevet distance. All of these are explained further and noted on [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator).  


## Student:

NameL Jacob Burke

School Email: jburke2@uoregon.edu

Personal Email: jwburke256@gmail.com

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
