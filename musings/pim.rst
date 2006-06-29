====================
I want a PIM that...
====================

:Author: Morten Lied Johansen
:Contact: mortenjo@ifi.uio.no

Introduction
============

This is just a quick bit of text outlining (and in some cases detailing) what I 
want from a PIM (Personal Information Manager). I'll list the general 
requirements first, and go into detail for each point afterwards.

Requirements
============

I want a PIM with stress on the M. Lots of PIMs today have extended beyond 
simply managing information, they want to distribute it aswell, with integrated 
E-mail etc. I don't want that. I want a PIM that:

  - Has an addressbook_
  - Has a calendar_
  - Has a task-list_
  - Has a webinterface_
  - Supports `open standards`_ so that it works with my phone/PDA

Addressbook
-----------

The addressbook needs to support all the kind of operations I'd like to do with 
a list of contacts. Ideally, it should lay no restrictions on the kind of 
information I can associate with a certain person, it should allow me to group 
contacts in different ways, and it should be possible to sort and manage "like I 
want it to" however that might be.

More specifically, I want these features as an absolute minimum:

  - Store both work and home details
  - Store several (unlimited?) phone numbers and email-addresses with each      
    location
  - Store free-text notes related to the contact
  - Define primary addresses and phone numbers
  - Cross-reference with the task-list_ for common projects etc.
  - Cross-reference with the calendar_ for things like birthdates etc.

Calendar
--------

A calendar needs to keep me informed of all my events, and in some cases, other 
peoples events. It should preferably do so without limitations on what kind of 
events, or when or for how long an event can take place.

It would also need to have unlimited forward time, so that I could schedule 
events several years in advance. Systems in place for repeating items on 
arbitrary schedules would be needed, as well as arbitrary length.

The minimum features are:

  - Events that can be undefined time of day, defined time and length, or       
    special occation
  - Arbitrary repeat patterns for all event types
  - Definable start-of-week
  - Week numbering, as well as dates
  - Year, month, week and day views
  - Cross-reference with calendar_ and task-list_
  - Multiple alerts for each event

Task-list
---------

The task-list is the part of the PIM I'm least concerned with at the moment, but 
that can change as soon as I start working on projects with deadlines etc. But 
because I lack experience using one, I have only limited feature-requests. They 
are as follows:

  - Cross-reference with calendar_ and addressbook_
  - Prioritise tasks
  - Keep dependencies between tasks
  - Store free-text notes associated with each task

Webinterface
------------

In order for a PIM to be truly useful, it needs to be accessible as much of the 
time as possible, and one way to do that is to make sure there is a webinterface 
for those times when you are not in your regular location. Alternatively, a thin 
client running locally which can interact with your PIM over the internet could 
also be used, but it would need to be minimal so it could be downloaded and ran 
without poweruser rights on the current computer. Typically, this is complicated 
and a webinterface is probably best either way.

Some features needed for a functional webinterface are:

  - Access to all features of the PIM
  - Validating XHTML to ensure that it works correctly in all recent browsers
  - Calendar viewability by thirdparties, limited to events marked public
  - Remote sync with other PIM software

Open Standards
--------------

There are lots of ways for PIMs to exchange data, each new PIM bringing with it 
what seems like a new way to exchange data with it, making the old ways 
obsolete. This leads to a sort of keep up or be left behind mentality, you 
always need the latest software in order to be able to exchange data with other 
systems. To combat this, I want multi-tier support for export/import of data, so 
that I will always be able to get my PIM to work with other systems, even if I 
have to write scripts to do it myself.

In most cases, we just want something that works. If that fails, we wants 
something that probably works, and is easy to manhandle into working. If that 
fails too, we want something we definatly can twist and turn and make it fit any 
form we'd like.

To achieve this, using Open Standards for data exchange is paramount. The PIM 
should therefore support what seems the best choices at the moment:

  - SyncML: Emerging industry standard, complex
  - i/vCalendar & i/vCard: Established standards, somewhat cumbersome
  - plain ascii (CSV): Anyone can read and understand this
