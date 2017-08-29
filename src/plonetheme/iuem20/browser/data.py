# -*- coding: utf-8 -*-

from plone.app.textfield.value import RichTextValue

import datetime


lorem = """
Vivamus dictum, nunc a tincidunt semper, lectus justo maximus neque,
et pulvinar ipsum dolor at nisl. Maecenas porttitor dolor nec ante cursus
viverra. Maecenas massa nunc, semper vitae pulvinar at, semper
at metus. Cras a fermentum diam. Sed a lobortis
risus, efficitur tincidunt lorem.
"""

bio_fr_text = """
<h4>Savoir-faire opérationnels</h4>
<ul>
<li>Utiliser les méthodes de prévention et
de gestion des risques<br/></li>
</ul>
<h4>Lieu d'exercice</h4>
<ul>
<li>L’activité s’exerce généralement au sein d'un service informatique<br/>
</li>
</ul>
<h3>Dipl&ocirc;me exig&eacute;</h3>
<ul>
<li>Doctorat, diplôme d’ingénieur<br/></li>
</ul>
<h3>Formations et expérience professionnelle souhaitables</h3>
<ul><li>Filière informatique</li></ul>
"""

bio_en_text = """
<h2>The RichTextValue<a class='headerlink' href='#the-richtextvalue'
title='Permalink to this headline'>¶</a></h2>
<p>The <code class='docutils literal'><span class='pre'>RichText</span>
</code> field does not store a string. Instead, it stores a
<code class='docutils literal'><span class='pre'>RichTextValue</span>
</code> object. This is an immutable object that has the
following properties:</p>
<dl class='docutils'>
<dt><code class='docutils literal'><span class='pre'>raw</span></code></dt>
<dd>a unicode string with the original input markup;</dd>
<dt><code class='docutils literal'><span class='pre'>mimeType</span></code>
</dt>
<dd>the MIME type of the original markup, e.g.
<code class='docutils literal'><span class='pre'>text/html</span></code> or
<code class='docutils literal'><span class='pre'>text/structured</span>
</code>;</dd>
<dt><code class='docutils literal'><span class='pre'>encoding</span></code>
</dt>
<dd>the default character encoding used when transforming the input markup.
Most likely, this will be UTF-8;</dd>
<dt><code class='docutils literal'><span class='pre'>raw_encoded</span>
</code></dt>
<dd>the raw input encoded in the given encoding;</dd>
<dt><code class='docutils literal'><span class='pre'>outputMimeType</span>
</code></dt>
<dd>the MIME type of the default output, taken from the field at the time of
instantiation;</dd>
<dt><code class='docutils literal'><span class='pre'>output</span></code></dt>
<dd>a unicode object representing the transformed output. If possible, this
is cached persistently until the <code class='docutils literal'>
<span class='pre'>RichTextValue</span></code> is replaced with a
new one (as happens when an edit form is saved, for example).</dd>
</dl>
"""

bio_fr = RichTextValue(bio_fr_text, 'text/plain', 'text/html')
bio_en = RichTextValue(bio_en_text, 'text/plain', 'text/html')

missionA = {}
missionA['title'] = u'Première mission'
missionA['description'] = u'Il faut être très hardi pour aller là-bas !'
missionA['start_date'] = datetime.datetime(2016, 5, 1)
missionA['end_date'] = datetime.datetime(2016, 6, 1)
missionA['presentation_fr'] = bio_fr
missionA['display_en'] = True
missionA['presentation_en'] = bio_en
missionA['main_pict'] = u'benthos.jpg'
missionA['pict_author'] = u'S. Hervé'
missionA['doc'] = None
missionA['zoom'] = 6
missionA['map_center'] = u'[48.40003249610685, -4.5263671875]'

missionB = {}
missionB['title'] = u'Deuxième mission'
missionB['description'] = u'Et là, on a de la chance de revenir entiers !'
missionB['start_date'] = datetime.datetime(2016, 7, 21)
missionB['end_date'] = datetime.datetime(2016, 8, 10)
missionB['presentation_fr'] = bio_fr
missionB['display_en'] = True
missionB['presentation_en'] = bio_en
missionB['main_pict'] = u'hydrophone.jpg'
missionB['pict_author'] = u'H. Seb'
missionB['doc'] = None
missionB['zoom'] = 5
missionB['map_center'] = u'[53.15994678846807, -9.2724609375]'

missionC = {}
missionC['title'] = u'Troisième mission'
missionC['description'] = u'Et là, on a de la chance de revenir entiers !'
missionC['start_date'] = datetime.datetime(2015, 8, 21)
missionC['end_date'] = datetime.datetime(2015, 9, 10)
missionC['presentation_fr'] = bio_fr
missionC['display_en'] = True
missionC['presentation_en'] = bio_en
missionC['main_pict'] = u'hydrophone.jpg'
missionC['pict_author'] = u'H. Seb'
missionC['doc'] = None
missionC['zoom'] = 5
missionC['map_center'] = u'[51.570241445811234, -7.932128906249999]'

missionD = {}
missionD['title'] = u'Quatrième mission'
missionD['description'] = u'Et là, on a de la chance de revenir entiers !'
missionD['start_date'] = datetime.datetime(2015, 1, 21)
missionD['end_date'] = datetime.datetime(2015, 3, 10)
missionD['presentation_fr'] = bio_fr
missionD['display_en'] = True
missionD['presentation_en'] = bio_en
missionD['main_pict'] = u'hydrophone.jpg'
missionD['pict_author'] = u'H. Seb'
missionD['doc'] = None
missionD['zoom'] = 5
missionD['map_center'] = u'[49.32780711070416, -2.43896484375]'

missions = []
missions.append(missionA)
missions.append(missionB)
missions.append(missionC)
missions.append(missionD)


projectA = {}
projectA['title'] = u'Mon projet'
projectA['description'] = u'C est là qu on voit si ça colle'
projectA['categories'] = ['film-documentaire', 'enseignement']
projectA['start_date'] = datetime.datetime(2016, 4, 12)
projectA['end_date'] = datetime.datetime(2016, 11, 30)
projectA['presentation_fr'] = bio_fr
projectA['display_en'] = True
projectA['presentation_en'] = bio_en
projectA['main_pict'] = u'coupe1.jpg'
projectA['pict_author'] = u'E. Amice'
projectA['doc'] = None
projectA['zoom'] = 5
projectA['map_center'] = u'[48.40003249610685, -4.5263671875]'


projects = []
projects.append(projectA)


portraitA = {}
portraitA['family_name'] = u'Chauvaud'
portraitA['first_name'] = u'Laurent'
portraitA['email'] = u'l.c@univ-brest.fr'
portraitA['main_pict'] = u'chauvaud.jpg'
portraitA['pict_author'] = u'CC Chauv'
portraitA['thumb_pict'] = u'chauvaud-sq.jpg'
portraitA['bio_fr'] = bio_fr
portraitA['display_en'] = True
portraitA['bio_en'] = bio_en
portraitA['jobs'] = [u'plongeur', u'chercheur']
portraitA['status'] = u''
portraitA['affiliation1'] = u'CNRS'
portraitA['affiliation2'] = u'LEMAR'
portraitA['affiliation3'] = u'IUEM'
portraitA['personal_page'] = u'http://www.iuem.org/me'
portraitA['unit_page'] = u'http://www.iuem.org/unit'
portraitA['research'] = u'http://www.iuem.org/search'

portraitB = {}
portraitB['family_name'] = u'Archambault'
portraitB['first_name'] = u'Jean-Luc'
portraitB['email'] = u'la.A@canada.ca'
portraitB['main_pict'] = u'archambault.jpg'
portraitB['pict_author'] = u''
portraitB['thumb_pict'] = u'archambault-sq.jpg'
portraitB['bio_fr'] = bio_fr
portraitB['display_en'] = True
portraitB['bio_en'] = bio_en
portraitB['jobs'] = [u'plongeur', u'chercheur']
portraitB['status'] = u'Chercheur'
portraitB['affiliation1'] = u'UQAR'
portraitB['affiliation2'] = u'CANADIAN Univ'
portraitB['affiliation3'] = u''
portraitB['personal_page'] = u'http://www.canada.ca/me'
portraitB['unit_page'] = u'http://www.canada.ca/myUnity'
portraitB['research'] = u'http://www.canada.ca/research'

portraitC = {}
portraitC['family_name'] = u'Amice'
portraitC['first_name'] = u'Erwan'
portraitC['email'] = u'e.a@iuem.org'
portraitC['main_pict'] = u'amice.jpg'
portraitC['pict_author'] = u''
portraitC['thumb_pict'] = u'amice-sq.jpg'
portraitC['bio_fr'] = bio_fr
portraitC['display_en'] = False
portraitC['bio_en'] = bio_en
portraitC['jobs'] = [u'plongeur', u'photographe']
portraitC['status'] = u'Assistant ingénieur'
portraitC['affiliation1'] = u'CCNNRRSS'
portraitC['affiliation2'] = u'LEMAR'
portraitC['affiliation3'] = u''
portraitC['personal_page'] = u'http://www.cnrs.fr/me'
portraitC['unit_page'] = u'http://www.cnrs.fr/unit'
portraitC['research'] = u'http://www.cnrs.fr/search'

portraitD = {}
portraitD['family_name'] = u'Guarini'
portraitD['first_name'] = u'Jennifer'
portraitD['email'] = u'e.a@iuem.org'
portraitD['main_pict'] = u'guarini_jennifer.jpg'
portraitD['pict_author'] = u''
portraitD['thumb_pict'] = u'guarini_jennifer-sq.jpg'
portraitD['bio_fr'] = bio_fr
portraitD['display_en'] = True
portraitD['bio_en'] = bio_en
portraitD['jobs'] = [u'plongeur', u'photographe']
portraitD['status'] = u'Assistant ingénieur'
portraitD['affiliation1'] = u'CCNNRRSS'
portraitD['affiliation2'] = u'LEMAR'
portraitD['affiliation3'] = u''
portraitD['personal_page'] = u'http://www.cnrs.fr/me'
portraitD['unit_page'] = u'http://www.cnrs.fr/unit'
portraitD['research'] = u'http://www.cnrs.fr/search'

portraitE = {}
portraitE['family_name'] = u'Grall'
portraitE['first_name'] = u'Jacques'
portraitE['email'] = u'e.a@iuem.org'
portraitE['main_pict'] = u'grall.jpg'
portraitE['pict_author'] = u''
portraitE['thumb_pict'] = u'grall-sq.jpg'
portraitE['bio_fr'] = bio_fr
portraitE['display_en'] = True
portraitE['bio_en'] = bio_en
portraitE['jobs'] = [u'plongeur', u'photographe']
portraitE['status'] = u'Assistant ingénieur'
portraitE['affiliation1'] = u'CCNNRRSS'
portraitE['affiliation2'] = u'LEMAR'
portraitE['affiliation3'] = u''
portraitE['personal_page'] = u'http://www.cnrs.fr/me'
portraitE['unit_page'] = u'http://www.cnrs.fr/unit'
portraitE['research'] = u'http://www.cnrs.fr/search'

portraits = []
portraits.append(portraitA)
portraits.append(portraitB)
portraits.append(portraitC)
portraits.append(portraitD)
portraits.append(portraitE)

sts = {}
sts['title'] = u'Mon joli site d études'
sts['description'] = u'Et là, on a de la chance de revenir entiers !'
sts['presentation_fr'] = bio_fr
sts['display_en'] = True
sts['presentation_en'] = bio_en
sts['main_pict'] = u'hydrophone.jpg'
sts['pict_author'] = u'H. Seb'
sts['doc'] = None
sts['zoom'] = 5
sts['map_center'] = u'[49.781264058178365, -7.207031249999999]'
