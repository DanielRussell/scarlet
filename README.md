ATTENTION!  This fork was created to help migrate a legacy site.  I
**strongly** recommend you not use it.  I may delete this fork at any
moment.

-- DanielRussell 2022-07-22


What is Scarlet?
==

Scarlet is a Content Management System built with Django. Scarlet adopts many
of the conventions of the Django Admin and extends them to enable a superset of
functionality. There are however some trade offs with using Scarlet; Postgres
9.1+ is the only supported RDBM.

Cool Stuff
==

* Versioning - Sophisticated versioning is included right out of the box.

* Caching - Expire your pages when the content changes, not based on some some
arbitrary time interval. Intelligently invalidate the cache for groups of
related objects (for example, when you publish a new article, the cache for
both the homepage and the article list page can automatically invalidate.)

* Content Scheduling - Schedule when you want you content to go live. Schedule
different versions of a piece of content to go live on different days.

* Asset Manager - Scarlet includes a powerful Asset management tool that can
automatically organize, tag, and resize images and other types of assets.

Installation
==

Scarlet depends on *Pillow* >= 2.7.0. This is not included as a requirement in
setup.py as Pillow's installation is better managed by the target system's
package manager.

Once Pillow is installed, Scarlet can be installed via *pip*.

    pip install scarlet
