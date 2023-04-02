Um R leiksvæði
==============

Leiksvæðin eru öflug
--------------------

Í hverjum kafla koma fyrir R leiksvæði þar sem lesendur geta skrifað og keyrt eigin R kóða. Þessi leiksvæði styðja mjög marga R pakka og er hægt að teikna flottar myndir með þeim, eins og hér fyrir neðan. Takið sérstaklega eftir því að hægt er að stækka myndina með því að ýta á örvarnar.

.. datacamp::
    :lang: r

    options(scipen=999)  # turn-off scientific notation like 1e+48
    library(ggplot2)
    theme_set(theme_bw())  # pre-set the bw theme.
    data("midwest", package = "ggplot2")

    gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
        geom_point(aes(col=state, size=popdensity)) + 
        geom_smooth(method="loess", se=F) + 
        xlim(c(0, 0.1)) + 
        ylim(c(0, 500000)) + 
        labs(subtitle="Area Vs Population", 
        y="Population", 
        x="Area", 
        title="Scatterplot", 
        caption = "Source: midwest")

    gg

DataCamp
--------

Hugbúnaðurinn DataCamp (http://datacamp.com) er notaður til þess að keyra kóðanum í leiksvæðunum. Sá hugbúnaður styður ýmis umhverfi, þar með talið python eða SQL, en við notum aðeins R stuðning þess hér.

Vandamál með keyrslu
--------------------

Almennt ætti allur kóði að keyrast eðlilega, en höfundar fundu eina undantekningu við þessu. Þetta vandamál lýsti sig þannig að skilaboðin `Your session has been disconnected.` komu upp í hvert sinn sem reynt var að keyra kóða og kóðinn keyrðist ekki heldur. 

Þetta kemur fyrir ef vafrin sem er notaður er stilltur þannig að hann leyfi ekki svokallaða `third-party cookies`. Lausnin er því að leyfa þeim á viðkomandi vafra. Nákvæmari leiðbeiningar fyrir það er háð vafrananum en oft leynist stillingin undir "content", "privacy", "cookies" og þess háttar. Sem dæmi, má finna stillinguna í Chrome með því að fara í "Settings -> Advanced -> Content settings -> Cookies".


Ef einstaklingur er mótfallin því að leyfa öllum `third-party cookies` nægir að setja inn undantekningu fyrir slóðina "datacamp.com". Mikilvægt er að nota rétt snið þá fyrir undantekninguna, t.d. vill Chrome frá ``[*.]datacamp.com`` meðan Firefox vill fá ``https://datacamp.com``.
