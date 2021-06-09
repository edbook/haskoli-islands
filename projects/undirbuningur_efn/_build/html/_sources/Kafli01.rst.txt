Einingar og reikniaðferðir
==========================

Stærðfræði kemur mikið við sögu í efnafræði og gott er að hafa góð tök á algengum stærðfræðireglum, s.s. algebru. Hér á eftir eru stærðfræðireglur notaðar án frekari útskýringa en stærðfræðigrunnur er mikilvægur undirbúningur fyrir efnafræðinám.

Til eru upprifjunarvefir á edbook í `stærðfræði <http://edbook.hi.is/undirbuningur_stae/>`_ og `eðlisfræði <http://edbook.hi.is/undirbuningur_edl/>`_ sem hægt er að nota ef ókunnug stærðfræðiregla eða hugtök koma fyrir sjónir. :math:`\require{cancel}`

SI-einingakerfið
----------------

Í nær öllum löndum heims er notað samræmt mælikerfi, SI-einingakerfið, þar sem einkennandi stærðir heimsins hafa eigin grunneiningar.
Lengd hefur þar grunneininguna metri og tími grunneininguna sekúnda.

SI-grunneiningarnar eru sjö:

.. math::
 \begin{array}{c | c | c}
	  \text{Mælistærð} & \text{Eining} & \text{Tákn} \\ \hline
	  \text{Vegalengd} & \text{Metri} & m \\
    \text{Tími} & \text{Sekúnda} & s \\
    \text{Massi} & \text{Kílógramm} & kg\\
	  \text{Rafstraumur} & \text{Amper} & A\\
    \text{Hitastig} & \text{Kelvin} & K \\
    \text{Ljósstyrkur} & \text{Candela} & cd \\
    \text{Fjöldi} & \text{Mól} & n \\ \hline
  \end{array}

Hugtök eins og ljósstyrkur mun ekki koma hér fyrir, en fær að fljóta með.

Einingar fyrir aðrar stærðir eru settar saman úr grunneiningum SI-einingakerfisins.
*Hraði*, breyting á staðsetningu yfir eitthvert tímabil, hefur eininguna metrar á sekúndu (m/s).

Kelvin
~~~~~~

Eins og sjá á er SI-eining hitastigs kelvin en ekki celsíus. Þessir skalar eru þó nátengdir og celsíus skalinn er eins og kelvin skalinn, nema einungis hliðraður. Celsíus er skilgreint með núllpunkt við frostmark vatns, en kelvin skalinn skilgreinir núllpunkt við *alkul*, en það er algjört lágmarkshitastig. Vatn frýs aftur á móti við 273,15 kelvin, svo að skalarnir tengjast með jöfnunni:

.. math::

  T(K) = T(C) + 273,15 \text{ K}

Hér táknar :math:`T(\text{K})` hitastig í kelvin en :math:`T(\text{C})` hitastig í celsíus

.. note::
  Þegar hitastig er gefið upp á kelvinskalanum er ekki talað um gráður, þ.e. vatn frýs við 273,15 kelvin (ekki 273,15 gráður kelvin).

Forskeyti SI-kerfisins
~~~~~~~~~~~~~~~~~~~~~~

Þegar fengist er við stærri mælistærðir, svo sem langar vegalengdir, er unnið með marga metra.
Því hafa vísindamenn vanið sig á að kalla þúsund metra öðru nafni: einn kílómetra (:math:`1000 \text{m} = 1 \text{km}`). Þegar fengist er við litlar mælistærðir, svo sem þykkt á pappír, fást aðeins brot af heilum metrum.
Algengt er að nota millímetra, einn þúsundasta úr metra. Þetta er tekið saman í þessari töflu,
á milli kíló og millí eru:

.. math::
  \begin{array}{c|c|c}
    \text{Forskeyti} & \text{Tákn} & \text{Tugveldi} & \text{Margfeldi}\\ \hline
    \text{Kíló} & \text{k} & 10^{3} & 1000\\
    \text{Hektó} & \text{h} & 10^{2} & 100 \\
    \text{Deka} & \text{da} & 10^{1} & 10 \\
    \text{--} & \text{--} & 10^{0} & 1 \\
    \text{Desi} & \text{d} & 10^{-1} & 0.1\\
    \text{Centi} & \text{c} & 10^{-2} & 0.01\\
    \text{Millí} & \text{m} & 10^{-3} & 0.001 \\ \hline
  \end{array}

Við getum því lýst 10 metrum sem 1 dam, 100 dm eða 1000 cm. Í efnafræði er þó algengt að einungis sé notað tugveldi í stað forskeytis. Mikilvægt er þó að geta breytt á milli.


Í efnafræði er sjaldan fengist við risastór fyrirbæri (eins og stjörnuþokur úti í geimi) en oftar allra minnstu fyrirbærin (eins og rafeindir).
Fyrir þessi fyrirbæri þarf enn önnur forskeyti:

.. math::
  \begin{array}{c|c|c}
    \text{Forskeyti} & \text{Tákn} & \text{Tugveldi} & \text{Margfeldi}\\ \hline
    \text{Peta} & \text{P} & 10^{15} & 1 000 000 000 000 000 \\
    \text{Tera} & \text{T} & 10^{12} & 1 000 000 000 000 \\
    \text{Giga} & \text{G} & 10^{9} & 1 000 000 000 \\
    \text{Mega} & \text{M} & 10^{6} & 1 000 000 \\
    \text{Kíló} & \text{k} & 10^{3} & 1 000\\
    \text{--} & \text{--} & 10^0 & 1\\
    \text{Millí} & \text{m} & 10^{-3} & 0.001 \\
    \text{Míkró} & \mu & 10^{-6} & 0.000 001 \\
    \text{Nanó} & \text{n} & 10^{-9} & 0.000 000 001 \\
    \text{Píkó} & \text{p} & 10^{-12} & 0.000 000 000 001 \\
    \text{Femtó} & \text{f} & 10^{-15} & 0.000 000 000 000 001 \\ \hline
  \end{array}

.. note::
  Athugið að þegar fengist er við massa þá er SI-einingin kílógramm en ekki gramm.

Að breyta um forskeyti
~~~~~~~~~~~~~~~~~~~~~~

Þegar breytt er um forskeyti er til ein rétt leið til að stytta út einingarnar.

Ef það á að breyta úr grömmum í kíló fæst að

.. math::

  1000 \text{ g} = 1 \text{ kg}

Ef deilt er í gegn með :math:`1000 \text{ g}` fæst:

.. math::

 1 = \frac{1\text{ kg}}{1000 \text{ g}}

Í algebru má alltaf margfalda með 1, og því má alltaf margfalda með hægri hlið jöfnunnar líka. Við það styttist út grömm og kílógrömm standa eftir.

.. tip::

 **Hvað eru 14 millígrömm mörg nanógrömm?**

 Hér er best að breyta fyrst í grömm, og svo aftur í nanógrömm:

 .. math::

   14 \bcancel{\text{ mg}} \cdot \frac{ 1\bcancel{\text{ g}}}{10^3 \bcancel{\text{ mg}}} \cdot \frac{10^9 \text{ ng}}{1 \bcancel{\text{ g}}} =14 \times 10^3 \text{ ng}


Markverðir tölustafir
---------------------

*Markverðir tölustafir* (e. Significant figures) segir til um nákvæmni mælingu. Nákvæmni útkomu reikninga byggist sterklega á nákvæmni mælingar. Því fleiri markverðir tölustafi sem mæling hefur, því nákvæmari er hún. Til dæmis má segja að ákveðinn maður er 2 m, 1,8 m, 183 cm eða 183,2 cm. Þessar tölur lýsa allar hæð mannsins, en með mismunandi fjölda af markverðum tölustöfum.

Tölustafir sem teljast vera markverðir eru allir tölustafir taldir frá vinstri þangað til einungis eru 0 hægra megin.

.. math::

  \begin{array} {c|c}
  \text{Tölur} & \text{Markverðir tölustafir}\\
  \hline
  12   & 2 \\
  1200  & 2 \\
  1302 & 4 \\
  \end{array}

1200 getur einnig haft fjóra markverða tölustafi og þyrfti frekari upplýsingar til að ákvarða það. Ef sagt væri að trjágrein væri 1200 cm gæti verið að það hafi verið mælt sem 12 metrar með mælitæki sem mældi einungis í metrum, eða nákvæmlega 1200 cm með málbandi sem mælir í sentimetrum. Í
fyrra tilvikunu væri einungis tveir markverðir stafir, en fjórir í því seinna.

Til aðgreiningar er hægt að taka fram töluna í tugaveldi, þ.e. hægt er að skrifa töluna sem

.. math::

  \begin{array} {c|c}
  \text{Tölur} & \text{Markverðir tölustafir}\\
  \hline
  1,2\times 10^2  & 2 \\
  1,200 \times 10^2  & 4 \\
  \end{array}

Fyrir *tugabrot* teljast allir tölustafir markverðir, sem hafa ekki einungis núll vinstra megin.

.. math::

  \begin{array} {c|c}
  \text{Tölur} & \text{Markverðir tölustafir}\\
  \hline
  1200  & 2-4 \\
  1200,1   & 5 \\
  0,0000032 & 2\\
  0,3000002 & 7\\
  \end{array}

Ef þessar reglur gleymast er alltaf hægt að skrifa tölurnar í tugaveldi, og athugað hve marga tölustafi þurfa að koma fram. Við það detta úr ómarkverð núll.

.. math::

  \begin{array} {c|c}
  \text{Tölur} & \text{Markverðir tölustafir}\\
  \hline
  3,2 \times 10^{-6} & 2\\
  3,000002 \times 10^{-1}& 7
  \end{array}

Samlagning og margföldun
~~~~~~~~~~~~~~~~~~~~~~~~

Þegar mælingar eru notaðar til að reikna fleiri gildi, takmarkast markverðir tölustafir svarsins við markverðu tölustafi upphafsgildanna.
Þetta gerist á tvo mögulega vegu og fer það eftir hvort notuð sé samlagning eða margföldun.

1 - Fyrir *margföldun* eða *deilingu* tveggja talna hefur útkoman jafn marga markverða tölustafi og upphafsgildið með færri markverða tölustafi.

.. math::

  5,02 (3) \cdot 8,0000 (5) &= 40,2 (3)\\

  \small{ (\text{Markverðir tölustafir})}

2 - Fyrir *samlagningu* skiptir einungis máli markverðir tölustafir *eftir* kommu, þ.e. tugabrot. Útkoman fær sama fjölda markverða stafi eftir kommu og upphafsgildið með færri markverða tölustafi eftir kommu.

.. math::

  53,024 (3)+ 310,3 (1) = 363,3 (1)\\
  \small{ (\text{Markverðir tölustafir eftir kommu})}

Ef gerðar eru margar aðgerðir, skal halda ríflegum fjölda af tölustöfum til haga þangað til lokasvarið fæst. Þá er fundnar þær aðgerðir sem takmarka fjölda markverðra stafa, og lokasvarið gefið með þeim fjölda af markverðum stöfum.

.. tip::

 **Hvert er lokasvarið, með réttum fjölda markverða stafa?**

  .. math::

    (53,467 + 41,22) \cdot 12,212 \cdot 14,00

 Hér liggur beint við að stinga allri jöfnunni í reiknivél en skulum þó taka þetta skref fyrir skref í þetta skiptið. Fyrst um sinn skal halda utan um þónokkra aukastafi:

  .. math::

    \begin{aligned}
    53,467 + 61,22 &= 114,687 \\
    114,687 \cdot 12,212 &= 1400,558 \\
    1156,318 \cdot 14,00 &= 19607,81 \\
    \end{aligned}

 Þá þarf að finna hve marga markverðu tölustafi svarið á að hafa. Byrjum á að finna markverða tölustafi í samlagningunni. Samlagningin er takmörkuð af tveimur aukastöfum, þ.e. 114,69 sem þýðir að það eru *fimm* markverðir stafir. Þá er einungis margföldunaraðgerðir eftir:

  .. math::


    (5) \cdot (5) \cdot (4) = (4)\\
    \small{ (\text{Markverðir tölustafir})}

 Þetta þýðir að lokasvarið skal gefið með *fjórum* markverðum stöfum, þ.e.

  .. math::

    (53,467 + 41,22) \cdot 12,212 \cdot 14,00 = 19610
