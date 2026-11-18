Hermun
======

Hvað er hermun og af hverju er hún gagnleg?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Óformlega höfum við hugsað um slembistærð svona: Gildið sem hún tekur fer eftir útkomunni úr einhverri tilraun sem er háð tilviljun eins og krónukasti eða teningakasti. Til dæmis, ef krónu er kastað og líkurnar á að þorskurinn komi upp eru :math:`p \in (0,1)`, þá höfum við kynnt til sögunnar Bernoulli-stærð :math:`X` sem tekur gildið :math:`X=1` þegar þorskurinn kemur upp og :math:`X=0` þegar bergrisinn kemur upp. Hingað til höfum við fjallað um líkurnar á að slembistærð taki eitthvert gildi (strjál slembistærð) eða að hún taki gildi á einhverju bili (samfelld slembistærð), en við höfum ekki fjallað um hvernig á að ,,raungera“ slembistærðina.

Að *herma* slembistærð er að gefa henni gildi með aðferð sem tryggir að líkurnar á að gildið komi upp samræmist líkindadreifingu slembistærðarinnar. Við segjum líka að við ,,búum til“, ,,framleiðum“ eða ,,raungerum“ slembistærðina. Í umfjölluninni sem fylgir gerum við ráð fyrir að við getum raungert jafna dreifingu á bilinu :math:`(0,1)`, þ.e. að við getum valið tölu af handahófi milli 0 og 1. Ýmsum aðferðum má beita til þess sem eru utan umfjöllunarefnis þessa námskeiðs. Við ætlum hins vegar að sýna hvernig hægt er að nota tölur sem valdar eru af handahófi milli 0 og 1 til að búa til slembistærðir með þekktar líkindadreifingar.

Hermun er mjög gagnleg þegar við vinnum með slembistærð eða slembiferli sem við þekkjum lítið og við viljum skilja hegðun t.d. slembiferlisins betur. Oftast er fljótlegra að herma slembiferlið og sjá hvað gerist en að leiða hegðunina út stærðfræðilega. Einnig getur hermunin verið vegvísir fyrir stærðfræðilegu greininguna. Hermun er loks gagnleg þegar unnið er með mjög flókið slembiferli sem erfitt er að greina stærðfræðilega. Hermunarlíkön geta t.d. verið notuð til að spá fyrir um hraunflæði á Reykjanesskaga og leggja mat á hversu líklegar tilteknar sviðsmyndir eru, þau eru notuð innan verkfræði til að skilja og hanna flókin kerfi og þau eru mjög vinsæl innan fjármálageirans þar sem þau eru kennd við *Monte Carlo* aðferðir.

Hermun á krónukasti
~~~~~~~~~~~~~~~~~~~

Fyrir jafndreifða stærð :math:`U` á bilinu :math:`(0,1)` og :math:`p \in (0,1)` gildir að

.. math:: \mathbb{P}(U < p) = \mathbb{P}(U \leq p) = p.

Skilgreinum slembistærðina :math:`X` þannig að hún sé háð gildinu á :math:`U` á eftirfarandi hátt:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    X = \begin{cases} 1, & \text{ef $U < p$}, \\ 0, & \text{ef $U \geq p$.} \end{cases}
   \end{aligned}
   \]

Takið eftir að :math:`X` er Bernoulli-stærð með stika :math:`p`, vegna þess að

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(X = 1) = \mathbb{P}(U < p) = p
   \end{aligned}
   \]

og :math:`\mathbb{P}(X=0)=\mathbb{P}(U \geq p) = 1-p`. Við getum þess vegna raungert Bernoulli-stærð út frá tölu sem er valin af handahófi milli 0 og 1, eins og við sýnum í R hér að neðan. Munið síðan úr Lík&töl að tvíkostastærð með stika :math:`n` og :math:`p` er hægt að hugsa sem summu af Bernoulli-stærðum,

.. math::
   :nowrap:

   \[
   \begin{aligned}
    X = X_1+X_2+\cdots+X_n,
   \end{aligned}
   \]

þar sem :math:`X_1,X_2,\ldots,X_n` eru óháðar Bernoulli-stærðir með stika :math:`p`. Þetta gefur einfalda aðferð til að herma tvíkostastærð.

Lögmál mikils fjölda
~~~~~~~~~~~~~~~~~~~~

Látum :math:`X` vera gefna slembistærð og látum :math:`X_1,X_2,\ldots` vera óháðar slembistærðir sem allar hafa sömu dreifingu og :math:`X`. Skilgreinum :math:`\bar{X}_n := \frac1n \sum_{i=1}^n X_i` sem meðalgildið sem fyrstu :math:`n` slembistærðirnar taka. *Lögmál mikils fjölda* segir óformlega að :math:`\bar{X}_n` nálgist væntigildið :math:`\mu = \mathbb{E}[X]` eftir því sem :math:`n` stækkar. Í hermunarsamhenginu segir lögmál mikils fjölda að ef við hermum óháð gildi fyrir slembistærðina :math:`X`, og reiknum meðaltal gildanna sem fást með hermuninni, þá nálgumst við væntigildið :math:`\mu` eftir því sem við hermum fleiri gildi.

Látum :math:`X_1,X_2,\ldots` vera óháðar Bernoulli-stærðir með stika :math:`p \in (0,1)`. Í þessu tilviki lýsir :math:`\bar{X}_n = \frac1n \sum_{i=1}^n X_i` hlutfallstíðni atburðarins að þorskurinn komi upp yfir fyrstu :math:`n` köstin. Væntigildi Bernoulli-stærðar með stika :math:`p` er

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{E}[X_1] = p \cdot 1 + (1-p) \cdot 0 = p.
   \end{aligned}
   \]

Fyrir Bernoulli-stærð með stika :math:`p` segir lögmál mikils fjölda að ef við hermum óháð krónuköst aftur og aftur, þá nálgast hlutfallstíðni atburðarins að þorskurinn komi upp einfaldlega líkurnar :math:`p` á atburðinum. Til að fá betri tilfinningu fyrir lögmáli mikils fjölda hermum við Bernoulli-stærðina í R.

.. rubric:: Hermun á krónukasti

.. code-block:: r

   #Fall sem hermir Bernoulli-stærð (krónukast) N sinnum.
   #p eru líkurnar á að þorskurinn komi upp.
   kronukast_hermun <- function(N,p){
     #results_vec er vigur sem geymir hermdu gildin.
     results_vec <- c(1:N)
     #Hermum N gildi fyrir Bernoulli stærð með stika p.
     for (j in 1:N){
         #Veljum tölu u af handahófi milli 0 og 1.
         u <- runif(1,0,1)
         #Búum til Bernoulli-stærð með stika p með því að nota gildið á u.
         #(u<p) gefur gildið TRUE ef u<p og gildið FALSE annars,
         #sem breytist í 1/0 þegar við vistum í vigurinn results_vec.
         results_vec[j] <- (u<p)
     }
     #Skilum vigrinum með hermdu gildunum.
     return(results_vec)
   }

Búum síðan til fall sem tekur inn hermd gildi fyrir Bernoulli-stærð með stika :math:`p` og teiknar samanburðarmynd sem ber saman hlutfallstíðnir gildanna sem hermunin gefur og massafall Bernoulli-dreifingar með stika :math:`p`. Samkvæmt lögmáli mikils fjölda eiga hlutfallstíðnirnar að nálgast massafallið eftir því sem við hermum fleiri gildi.

.. rubric:: Samanburður á hermdri hlutfallstíðni og massafalli Bernoulli-dreifingar

.. code-block:: r

   #Notum ggplot2 til að teikna.
   library(ggplot2)
   #Þessi valkostur sýnir tölur eins og 10^5 sem 100000.
   options(scipen=999)
   #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallstíðni
   #gildanna í hermuninni við massafall Bernoulli-dreifingar með stika p.
   teikna_kronukast <- function(results_vec,p){
     #Finnum stærsta gildið sem kom út úr hermuninni.
     max_gildi <- max(results_vec)
     #Reiknum hlutfallstíðni hermdu gildanna.
     #hist býr til tíðnitöflu (e. histogram) þar sem (-1:y)+0.5
     #skilgreinir bilin sem notuð eru til að útbúa tíðnitöfluna.
     #"plot = FALSE" segir R að teikna ekki stuðlaritið (við gerum það síðar).
     tidnirit <- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
     #Búum til gagnasafn sem geymir gögnin fyrir hermdu hlutfallstíðnirnar.
     hlutfallstidni <- data.frame(
       x_gildi = 0:max_gildi,
       #tidnirit$density gefur hlutfallstíðnirnar
       y_gildi = tidnirit$density, 
       audkenni="Hermd hlutfallstíðni"
     )
     #Búum til gagnasafn sem geymir massafall Bernoulli-dreifingar með stika p.
     bernoulli_massafall <- data.frame(
       x_gildi = 0:max_gildi,
       y_gildi = dbinom(0:max_gildi, 1, p),
       audkenni="Massafall Bernoulli-dreifingar"
     )
     #Sameinum gagnasöfnin
     sameinud_gogn <- rbind(hlutfallstidni, bernoulli_massafall)
     #Teiknum samanburðarmyndina.
     ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
       #geom_bar teiknar stöplarit.
       #position = "dodge" teiknar tvö stöplarit hlið við hlið.
       #alpha = 0.8 stjórnar hversu ógegnsær liturinn er.
       geom_bar(stat = "identity", position = "dodge", alpha = 0.8) + 
       labs(title = paste("Niðurstöður fyrir p =",p,"og N =",N), caption = paste("Samanburður á hermdri hlutfallstíðni fyrir Bernoulli-stærð með stika p =",p,"\nog massafalli Bernoulli-dreifingar með stika p =",p), x = "Gildi slembistærðarinnar", y ="") +
       scale_fill_manual(name="", values = c("Hermd hlutfallstíðni" = 'steelblue3', "Massafall Bernoulli-dreifingar" = 'brown3')) + 
       theme(plot.caption=element_text(size=11, hjust=0, face="italic", color="black"))
   }

.. rubric:: Gagnvirkur R-leikvöllur

.. raw:: html

   <div data-datacamp-exercise data-lang="r" data-height="600">
     <code data-type="pre-exercise-code">
       try(Sys.setlocale(&#39;LC_CTYPE&#39;, &#39;C.UTF-8&#39;), silent=TRUE)

       #Fall sem hermir Bernoulli-st\u00E6r\u00F0 (kr\u00F3nukast) N sinnum.
       #p eru l\u00EDkurnar \u00E1 a\u00F0 \u00FEorskurinn komi upp.
       kronukast_hermun &lt;- function(N,p){
         #results_vec er vigur sem geymir hermdu gildin.
         results_vec &lt;- c(1:N)
         #Hermum N gildi fyrir Bernoulli st\u00E6r\u00F0 me\u00F0 stika p.
         for (j in 1:N){
             #Veljum t\u00F6lu u af handah\u00F3fi milli 0 og 1.
             u &lt;- runif(1,0,1)
             #B\u00FAum til Bernoulli-st\u00E6r\u00F0 me\u00F0 stika p me\u00F0 \u00FEv\u00ED a\u00F0 nota gildi\u00F0 \u00E1 u.
             #(u&lt;p) gefur gildi\u00F0 TRUE ef u&lt;p og gildi\u00F0 FALSE annars,
             #sem breytist \u00ED 1/0 \u00FEegar vi\u00F0 vistum \u00ED vigurinn results_vec.
             results_vec[j] &lt;- (u&lt;p)
         }
         #Skilum vigrinum me\u00F0 hermdu gildunum.
         return(results_vec)
       }

       #Notum ggplot2 til a\u00F0 teikna.
       library(ggplot2)
       #\u00DEessi valkostur s\u00FDnir t\u00F6lur eins og 10^5 sem 100000.
       options(scipen=999)
       #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallst\u00ED\u00F0ni
       #gildanna \u00ED hermuninni vi\u00F0 massafall Bernoulli-dreifingar me\u00F0 stika p.
       teikna_kronukast &lt;- function(results_vec,p){
         #Finnum st\u00E6rsta gildi\u00F0 sem kom \u00FAt \u00FAr hermuninni.
         max_gildi &lt;- max(results_vec)
         #Reiknum hlutfallst\u00ED\u00F0ni hermdu gildanna.
         #hist b\u00FDr til t\u00ED\u00F0nit\u00F6flu (e. histogram) \u00FEar sem (-1:y)+0.5
         #skilgreinir bilin sem notu\u00F0 eru til a\u00F0 \u00FAtb\u00FAa t\u00ED\u00F0nit\u00F6fluna.
         #&quot;plot = FALSE&quot; segir R a\u00F0 teikna ekki stu\u00F0lariti\u00F0 (vi\u00F0 gerum \u00FEa\u00F0 s\u00ED\u00F0ar).
         tidnirit &lt;- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
         #B\u00FAum til gagnasafn sem geymir g\u00F6gnin fyrir hermdu hlutfallst\u00ED\u00F0nirnar.
         hlutfallstidni &lt;- data.frame(
           x_gildi = 0:max_gildi,
           #tidnirit$density gefur hlutfallst\u00ED\u00F0nirnar
           y_gildi = tidnirit$density, 
           audkenni=&quot;Hermd hlutfallst\u00ED\u00F0ni&quot;
         )
         #B\u00FAum til gagnasafn sem geymir massafall Bernoulli-dreifingar me\u00F0 stika p.
         bernoulli_massafall &lt;- data.frame(
           x_gildi = 0:max_gildi,
           y_gildi = dbinom(0:max_gildi, 1, p),
           audkenni=&quot;Massafall Bernoulli-dreifingar&quot;
         )
         #Sameinum gagnas\u00F6fnin
         sameinud_gogn &lt;- rbind(hlutfallstidni, bernoulli_massafall)
         #Teiknum samanbur\u00F0armyndina.
         ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
           #geom_bar teiknar st\u00F6plarit.
           #position = &quot;dodge&quot; teiknar tv\u00F6 st\u00F6plarit hli\u00F0 vi\u00F0 hli\u00F0.
           #alpha = 0.8 stj\u00F3rnar hversu \u00F3gegns\u00E6r liturinn er.
           geom_bar(stat = &quot;identity&quot;, position = &quot;dodge&quot;, alpha = 0.8) + 
           labs(title = paste(&quot;Ni\u00F0urst\u00F6\u00F0ur fyrir p =&quot;,p,&quot;og N =&quot;,N), caption = paste(&quot;Samanbur\u00F0ur \u00E1 hermdri hlutfallst\u00ED\u00F0ni fyrir Bernoulli-st\u00E6r\u00F0 me\u00F0 stika p =&quot;,p,&quot;\nog massafalli Bernoulli-dreifingar me\u00F0 stika p =&quot;,p), x = &quot;Gildi slembist\u00E6r\u00F0arinnar&quot;, y =&quot;&quot;) +
           scale_fill_manual(name=&quot;&quot;, values = c(&quot;Hermd hlutfallst\u00ED\u00F0ni&quot; = &#39;steelblue3&#39;, &quot;Massafall Bernoulli-dreifingar&quot; = &#39;brown3&#39;)) + 
           theme(plot.caption=element_text(size=11, hjust=0, face=&quot;italic&quot;, color=&quot;black&quot;))
       }
     </code>
     <code data-type="sample-code">
       # Velji\u00F0 N og p og keyri\u00F0 hermunina.
       N &lt;- 10000
       p &lt;- 0.5
       gildi &lt;- kronukast_hermun(N, p)
       teikna_kronukast(gildi, p)
     </code>
   </div>

Látum :math:`(\Omega,{\cal F},\mathbb{P})` vera líkindarúm. Munið að kennifall atburðar :math:`A \in {\cal F}` var slembistærðin :math:`1_A: \Omega \to \mathbb{R}` sem skilgreind var svona:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    1_A(\omega) := \begin{cases} 1, & \text{ef $\omega \in A$,} \\ 0, & \text{ef $\omega \notin A$.} \end{cases}
   \end{aligned}
   \]

Takið eftir að :math:`1_A` er Bernoulli-stærð með stika :math:`p = \mathbb{P}(A)`. Ímyndum okkur að atburðurinn :math:`A` sé tengdur einhverri tilraun eins og teningakasti. Ef við beitum lögmáli mikils fjölda á stærðina :math:`1_A`, þá segir lögmálið að ef við endurtökum tilraunina aftur og aftur, þá nálgast hlutfallstíðni þess að atburðurinn :math:`A` gerist einfaldlega líkurnar á atburðinum :math:`\mathbb{P}(A)`. Hermum tvíkostastærð í R og sjáum að hlutfallstíðnir gildanna nálgist líkurnar á að stærðin taki hvert gildi.

.. rubric:: Hermun á tvíkostastærð

.. code-block:: r

   #Fall sem hermir tvíkostastærð N sinnum.
   #n og p eru stikar tvíkostastærðarinnar.
   tvikostastaerd_hermun <- function(N,n,p){
     #results_vec er vigur sem geymir hermdu gildin.
     results_vec <- c(1:N)
     #Hermum N gildi fyrir tvíkostastærð með stika n og p.
     for (j in 1:N){
         #Hermum n Bernouli-stærðir með stika p 
         #með kóðanum sem við bjuggum til að ofan.
         x <- kronukast_hermun(n,p)
         #Búum til tvíkostastærð með því að leggja saman gildi Bernoulli-stærðanna.
         results_vec[j] <- sum(x)
     }
     #Skilum vigrinum með hermdu gildunum.
     return(results_vec)
   }

Búum síðan til fall sem tekur inn hermd gildi fyrir tvíkostastærð með stika :math:`n` og :math:`p` og teiknar samanburðarmynd sem ber saman hlutfallstíðnir gildanna sem hermunin gefur og massafall tvíkostadreifingar með stika :math:`n` og :math:`p`. Athugið að kóðinn er mjög svipaður og kóðinn sem við notuðum fyrir Bernoulli-dreifinguna að ofan.

.. rubric:: Samanburður á hermdri hlutfallstíðni og massafalli tvíkostdreifingar

.. code-block:: r

   #Notum ggplot2 til að teikna.
   library(ggplot2)
   #Þessi valkostur sýnir tölur eins og 10^5 sem 100000.
   options(scipen=999)
   #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallstíðni
   #gilda í hermuninni við massafall tvíkostadreifingar með stika n og p.
   teikna_tvikostastaerd <- function(results_vec,n,p){
     #Finnum stærsta gildið sem kom út úr hermuninni.
     max_gildi <- max(results_vec)
     #Reiknum hlutfallstíðni hermdu gildanna.
     tidnirit <- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
     #Búum til gagnasafn sem geymir gögnin fyrir hermdu hlutfallstíðnirnar.
     hlutfallstidni <- data.frame(
       x_gildi = 0:max_gildi,
       #tidnirit$density gefur hlutfallstíðnirnar
       y_gildi = tidnirit$density, 
       audkenni="Hermd hlutfallstíðni"
     )
     #Búum til gagnasafn sem geymir massafall tvíkostadreifingar með stika n og p.
     tvikosta_massafall <- data.frame(
       x_gildi = 0:max_gildi,
       y_gildi = dbinom(0:max_gildi, n, p),
       audkenni="Massafall tvíkostadreifingar"
     )
     #Sameinum gagnasöfnin
     sameinud_gogn <- rbind(hlutfallstidni, tvikosta_massafall)
     ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
       #Notum geom_bar til að teikna stöplarit.
       geom_bar(stat = "identity", position = "dodge", alpha = 0.8) + 
       labs(title = paste("Niðurstöður fyrir p =",p,"og N =",N), caption = paste("Samanburður á hermdri hlutfallstíðni fyrir tvíkostastærð með stika n =",n,"og p =",p,"\nog massafalli tvíkostadreifingar með stika n =",n,"og p =",p), x = "Gildi slembistærðarinnar", y ="") +
       scale_fill_manual(name="", values = c("Hermd hlutfallstíðni" = 'steelblue3', "Massafall tvíkostadreifingar" = 'brown3')) + 
     theme(plot.caption=element_text(size=11, hjust=0, face="italic", color="black"))
   }

.. rubric:: Gagnvirkur R-leikvöllur

.. raw:: html

   <div data-datacamp-exercise data-lang="r" data-height="600">
     <code data-type="pre-exercise-code">
       try(Sys.setlocale(&#39;LC_CTYPE&#39;, &#39;C.UTF-8&#39;), silent=TRUE)

       #Fall sem hermir Bernoulli-st\u00E6r\u00F0 (kr\u00F3nukast) N sinnum.
       #p eru l\u00EDkurnar \u00E1 a\u00F0 \u00FEorskurinn komi upp.
       kronukast_hermun &lt;- function(N,p){
         #results_vec er vigur sem geymir hermdu gildin.
         results_vec &lt;- c(1:N)
         #Hermum N gildi fyrir Bernoulli st\u00E6r\u00F0 me\u00F0 stika p.
         for (j in 1:N){
             #Veljum t\u00F6lu u af handah\u00F3fi milli 0 og 1.
             u &lt;- runif(1,0,1)
             #B\u00FAum til Bernoulli-st\u00E6r\u00F0 me\u00F0 stika p me\u00F0 \u00FEv\u00ED a\u00F0 nota gildi\u00F0 \u00E1 u.
             #(u&lt;p) gefur gildi\u00F0 TRUE ef u&lt;p og gildi\u00F0 FALSE annars,
             #sem breytist \u00ED 1/0 \u00FEegar vi\u00F0 vistum \u00ED vigurinn results_vec.
             results_vec[j] &lt;- (u&lt;p)
         }
         #Skilum vigrinum me\u00F0 hermdu gildunum.
         return(results_vec)
       }

       #Fall sem hermir tv\u00EDkostast\u00E6r\u00F0 N sinnum.
       #n og p eru stikar tv\u00EDkostast\u00E6r\u00F0arinnar.
       tvikostastaerd_hermun &lt;- function(N,n,p){
         #results_vec er vigur sem geymir hermdu gildin.
         results_vec &lt;- c(1:N)
         #Hermum N gildi fyrir tv\u00EDkostast\u00E6r\u00F0 me\u00F0 stika n og p.
         for (j in 1:N){
             #Hermum n Bernouli-st\u00E6r\u00F0ir me\u00F0 stika p 
             #me\u00F0 k\u00F3\u00F0anum sem vi\u00F0 bjuggum til a\u00F0 ofan.
             x &lt;- kronukast_hermun(n,p)
             #B\u00FAum til tv\u00EDkostast\u00E6r\u00F0 me\u00F0 \u00FEv\u00ED a\u00F0 leggja saman gildi Bernoulli-st\u00E6r\u00F0anna.
             results_vec[j] &lt;- sum(x)
         }
         #Skilum vigrinum me\u00F0 hermdu gildunum.
         return(results_vec)
       }

       #Notum ggplot2 til a\u00F0 teikna.
       library(ggplot2)
       #\u00DEessi valkostur s\u00FDnir t\u00F6lur eins og 10^5 sem 100000.
       options(scipen=999)
       #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallst\u00ED\u00F0ni
       #gilda \u00ED hermuninni vi\u00F0 massafall tv\u00EDkostadreifingar me\u00F0 stika n og p.
       teikna_tvikostastaerd &lt;- function(results_vec,n,p){
         #Finnum st\u00E6rsta gildi\u00F0 sem kom \u00FAt \u00FAr hermuninni.
         max_gildi &lt;- max(results_vec)
         #Reiknum hlutfallst\u00ED\u00F0ni hermdu gildanna.
         tidnirit &lt;- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
         #B\u00FAum til gagnasafn sem geymir g\u00F6gnin fyrir hermdu hlutfallst\u00ED\u00F0nirnar.
         hlutfallstidni &lt;- data.frame(
           x_gildi = 0:max_gildi,
           #tidnirit$density gefur hlutfallst\u00ED\u00F0nirnar
           y_gildi = tidnirit$density, 
           audkenni=&quot;Hermd hlutfallst\u00ED\u00F0ni&quot;
         )
         #B\u00FAum til gagnasafn sem geymir massafall tv\u00EDkostadreifingar me\u00F0 stika n og p.
         tvikosta_massafall &lt;- data.frame(
           x_gildi = 0:max_gildi,
           y_gildi = dbinom(0:max_gildi, n, p),
           audkenni=&quot;Massafall tv\u00EDkostadreifingar&quot;
         )
         #Sameinum gagnas\u00F6fnin
         sameinud_gogn &lt;- rbind(hlutfallstidni, tvikosta_massafall)
         ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
           #Notum geom_bar til a\u00F0 teikna st\u00F6plarit.
           geom_bar(stat = &quot;identity&quot;, position = &quot;dodge&quot;, alpha = 0.8) + 
           labs(title = paste(&quot;Ni\u00F0urst\u00F6\u00F0ur fyrir p =&quot;,p,&quot;og N =&quot;,N), caption = paste(&quot;Samanbur\u00F0ur \u00E1 hermdri hlutfallst\u00ED\u00F0ni fyrir tv\u00EDkostast\u00E6r\u00F0 me\u00F0 stika n =&quot;,n,&quot;og p =&quot;,p,&quot;\nog massafalli tv\u00EDkostadreifingar me\u00F0 stika n =&quot;,n,&quot;og p =&quot;,p), x = &quot;Gildi slembist\u00E6r\u00F0arinnar&quot;, y =&quot;&quot;) +
           scale_fill_manual(name=&quot;&quot;, values = c(&quot;Hermd hlutfallst\u00ED\u00F0ni&quot; = &#39;steelblue3&#39;, &quot;Massafall tv\u00EDkostadreifingar&quot; = &#39;brown3&#39;)) + 
         theme(plot.caption=element_text(size=11, hjust=0, face=&quot;italic&quot;, color=&quot;black&quot;))
       }
     </code>
     <code data-type="sample-code">
       # Velji\u00F0 stika tv\u00EDkostadreifingarinnar og keyri\u00F0 hermunina.
       N &lt;- 10000
       n &lt;- 10
       p &lt;- 0.35
       gildi &lt;- tvikostastaerd_hermun(N, n, p)
       teikna_tvikostastaerd(gildi, n, p)
     </code>
   </div>

Hermun á veldsstærð
~~~~~~~~~~~~~~~~~~~

Hermum næst slembistærð sem hefur veldisdreifingu með stika :math:`\lambda`. Hún er samfelld slembistærð með þéttleikann

.. math::
   :nowrap:

   \[
   \begin{aligned}
    f(x) = \begin{cases} \lambda e^{-\lambda x}, & x \geq 0, \\ 0,& x<0. \end{cases}
   \end{aligned}
   \]

.. container:: center

   .. figure:: images/veldisstaerd_thettleiki_unnid.svg
      :width: 207.02pt
      :align: center

Eins og gildir fyrir Bernoulli- og tvíkostastærðir er hægt að herma veldisstærð með því að velja fyrst tölu af handahófi milli 0 og 1. Nánar tiltekið, ef :math:`U` hefur jafna dreifingu á :math:`(0,1)`, þá er tiltölulega einfalt að sýna að

.. math:: X := -\ln(U)/\lambda

hefur veldisdreifingu með stika :math:`\lambda`. Hvernig er hægt að komast að því hvort svona fullyrðing sé rétt? Ein leið er að sanna það stærðfræðilega, sem þið gerið í skiladæmunum. En hér er hermun líka fljótleg og gagnleg leið til að kanna hvort fullyrðingin sé rétt. Förum í R til að herma.

.. rubric:: Hermun á veldisstærð

.. code-block:: r

   #Fall sem hermir veldisstærð N sinnum.
   #lambda er stiki veldisstaerdarinnar.
   veldisstaerd_hermun <- function(N,lambda){
     #results_vec er vigur sem geymir hermdu gildin.
     results_vec <- c(1:N)
     for(j in 1:N){
       #Veljum tölu u af handahófi milli 0 og 1.
       u <- runif(1, 0, 1)
       #Búum til veldisstærð með stika p með því að nota gildið á u.
       #Athugið að log gefur náttúrulega logrann í R.
       results_vec[j] <- -log(u)/lambda
       }
     #Skilum vigrinum með hermdu gildunum.
     return(results_vec)  
   }

Þar sem við erum núna að vinna með samfellda slembistærð höfum við ekki áhuga á hlutfallstíðni einstakra gilda heldur höfum við áhuga á þéttleika gildanna. Við notum ``geom_density`` í R til að áætla þéttleika gildanna sem hermunin gefur og berum hann síðan saman við þéttleika veldisdreifingarinnar með stika :math:`lambda`.

.. rubric:: Samanburður á hermdri hlutfallstíðni og þéttleika veldisdreifingar

.. code-block:: r

   #Notum ggplot2 til að teikna.
   library(ggplot2)
   #Þessi valkostur sýnir tölur eins og 10^5 sem 100000.
   options(scipen=999)
   #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hermdan þéttleika
   #við þéttleika veldisdreifingar með stika lambda.
   teikna_veldisstaerd <- function(results_vec,lambda){
     #Teiknum mynd.
     ggplot(data.frame(results_vec), aes(x = results_vec)) + 
     #geom_density tekur gildin í results_vec og notar þau til að reikna þéttleika.
     #bounds = c(0,Inf) segir geom_density að slembistærðin tekur aðeins jákvæð rauntölugildi.
     geom_density(linewidth = 2, bounds = c(0,Inf), aes(color = 'Hermdur þéttleiki')) + 
     #Notum stat_function til að teikna þéttleika veldisdreifingarinnar með stika lambda.
     #fun = dexp segir stat_function að nota þéttleika veldisdreifingarinnar.
     #args = list(rate = 2) segir stat_function að stiki dreifingarinnar sé lambda.
     stat_function(linewidth = 3, aes(color = 'Þéttleiki veldisdreifingar'),fun = dexp, args = list(rate = lambda), linetype="dotted") +
     labs(title = paste("Niðurstöður fyrir lambda =",lambda,"og N =",N), caption = paste("Samanburður á hermdum þéttleika fyrir -log(U)/lambda og\nþéttleika veldisdreifingar með stika lambda = ",lambda), x = "Gildi slembistærðarinnar", y ="") +
     scale_color_manual(name='', values = c('Hermdur þéttleiki' = 'steelblue3', 'Þéttleiki veldisdreifingar' = 'black')) + 
     theme(plot.caption=element_text(size=11, hjust=0, face="italic", color="black"))
   }

.. rubric:: Gagnvirkur R-leikvöllur

.. raw:: html

   <div data-datacamp-exercise data-lang="r" data-height="600">
     <code data-type="pre-exercise-code">
       try(Sys.setlocale(&#39;LC_CTYPE&#39;, &#39;C.UTF-8&#39;), silent=TRUE)

       #Fall sem hermir veldisst\u00E6r\u00F0 N sinnum.
       #lambda er stiki veldisstaerdarinnar.
       veldisstaerd_hermun &lt;- function(N,lambda){
         #results_vec er vigur sem geymir hermdu gildin.
         results_vec &lt;- c(1:N)
         for(j in 1:N){
           #Veljum t\u00F6lu u af handah\u00F3fi milli 0 og 1.
           u &lt;- runif(1, 0, 1)
           #B\u00FAum til veldisst\u00E6r\u00F0 me\u00F0 stika p me\u00F0 \u00FEv\u00ED a\u00F0 nota gildi\u00F0 \u00E1 u.
           #Athugi\u00F0 a\u00F0 log gefur n\u00E1tt\u00FArulega logrann \u00ED R.
           results_vec[j] &lt;- -log(u)/lambda
           }
         #Skilum vigrinum me\u00F0 hermdu gildunum.
         return(results_vec)  
       }

       #Notum ggplot2 til a\u00F0 teikna.
       library(ggplot2)
       #\u00DEessi valkostur s\u00FDnir t\u00F6lur eins og 10^5 sem 100000.
       options(scipen=999)
       #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hermdan \u00FE\u00E9ttleika
       #vi\u00F0 \u00FE\u00E9ttleika veldisdreifingar me\u00F0 stika lambda.
       teikna_veldisstaerd &lt;- function(results_vec,lambda){
         #Teiknum mynd.
         ggplot(data.frame(results_vec), aes(x = results_vec)) + 
         #geom_density tekur gildin \u00ED results_vec og notar \u00FEau til a\u00F0 reikna \u00FE\u00E9ttleika.
         #bounds = c(0,Inf) segir geom_density a\u00F0 slembist\u00E6r\u00F0in tekur a\u00F0eins j\u00E1kv\u00E6\u00F0 raunt\u00F6lugildi.
         geom_density(linewidth = 2, bounds = c(0,Inf), aes(color = &#39;Hermdur \u00FE\u00E9ttleiki&#39;)) + 
         #Notum stat_function til a\u00F0 teikna \u00FE\u00E9ttleika veldisdreifingarinnar me\u00F0 stika lambda.
         #fun = dexp segir stat_function a\u00F0 nota \u00FE\u00E9ttleika veldisdreifingarinnar.
         #args = list(rate = 2) segir stat_function a\u00F0 stiki dreifingarinnar s\u00E9 lambda.
         stat_function(linewidth = 3, aes(color = &#39;\u00DE\u00E9ttleiki veldisdreifingar&#39;),fun = dexp, args = list(rate = lambda), linetype=&quot;dotted&quot;) +
         labs(title = paste(&quot;Ni\u00F0urst\u00F6\u00F0ur fyrir lambda =&quot;,lambda,&quot;og N =&quot;,N), caption = paste(&quot;Samanbur\u00F0ur \u00E1 hermdum \u00FE\u00E9ttleika fyrir -log(U)/lambda og\n\u00FE\u00E9ttleika veldisdreifingar me\u00F0 stika lambda = &quot;,lambda), x = &quot;Gildi slembist\u00E6r\u00F0arinnar&quot;, y =&quot;&quot;) +
         scale_color_manual(name=&#39;&#39;, values = c(&#39;Hermdur \u00FE\u00E9ttleiki&#39; = &#39;steelblue3&#39;, &#39;\u00DE\u00E9ttleiki veldisdreifingar&#39; = &#39;black&#39;)) + 
         theme(plot.caption=element_text(size=11, hjust=0, face=&quot;italic&quot;, color=&quot;black&quot;))
       }
     </code>
     <code data-type="sample-code">
       # Velji\u00F0 lambda og keyri\u00F0 hermunina.
       N &lt;- 10000
       lambda &lt;- 2
       gildi &lt;- veldisstaerd_hermun(N, lambda)
       teikna_veldisstaerd(gildi, lambda)
     </code>
   </div>

Í hermunarverkefninu sjáum við að Poisson-dreifinguna er líka hægt að herma með því að velja tölur af handahófi milli 0 og 1. Nánar tiltekið: Ef við látum :math:`U_1,U_2,\ldots` vera óháðar slembistærðir með jafna dreifingu á bilinu :math:`(0,1)` og látum :math:`\lambda > 0`, þá hefur slembistærðin

.. math::
   :nowrap:

   \[
   \begin{aligned}
    X := \max\left\{n \geq 0: \prod_{i=1}^{n} U_i \geq e^{-\lambda}\right\}
   \end{aligned}
   \]

Poisson-dreifingu með stika :math:`\lambda`. Þetta er annað dæmi um gagnsemi hermunar: Það er alls ekki augljóst fyrirfram að þessi stærð hafi Poisson-dreifingu, en hermun er fljótleg leið til að staðfesta það.

Innbyggðar skipanir í R
~~~~~~~~~~~~~~~~~~~~~~~

Hingað til höfum við búið til okkar eigin hermunarkóða með því að velja tölur af handahófi milli 0 og 1 og nota þær til að herma slembistærðir t.d. með Bernoulli-, tvíkosta- og veldisdreifinguna. Hins vegar eru líka til innbyggðar skipanir í R sem herma beint slembistærðir með þekktar líkindadreifingar. Förum í R og tökum dæmi um tvíkosta- og veldisdreifinguna.

.. container:: center

   ========================== ===========================
   Dreifing                   Skipun til að herma N gildi
   ========================== ===========================
   :math:`{\rm Ber}(p)`       ``rbinom(N,1,p)``

   :math:`{\rm Bin}(n,p)`     ``rbinom(N,n,p)``

   :math:`{\rm Poi}(\lambda)` ``rpois(N,lambda)``

   :math:`{\rm Unf}[a,b]`     
                              ``runif(N,a,b)``

   :math:`{\rm Exp}(\lambda)` ``rexp(N,lambda)``

   :math:`N(\mu,\sigma)`      ``rnorm(N,mu,sigma)``
   ========================== ===========================

Hermun á Poisson-ferlum
~~~~~~~~~~~~~~~~~~~~~~~

Í Lík&töl settum við fram líkan fyrir komur á bráðamóttökuna yfir eina klukkustund. Hugmyndin var að búta eina klukkustund niður í stutt hlutbil af lengdinni :math:`1/n`, þannig að í mesta lagi ein koma verði á hverju hlutbili, og gera ráð fyrir að líkurnar á komu væru :math:`p = \lambda/n` fyrir hvert og eitt hlutbil, þar sem :math:`\lambda>0` var einhver jákvæð rauntala. Við getum hugsað stikann :math:`\lambda` sem meðalfjöldi koma sem verður yfir eina klukkustund.

.. container:: center

   .. figure:: images/poisson_dreifing_2.svg
      :width: 251.44pt
      :align: center

.. container:: center

   .. figure:: images/poisson_dreifing_3.svg
      :width: 294.2pt
      :align: center

Fjölda koma er hægt að lýsa með tvíkostastærð þar sem fjöldi tilrauna er :math:`n` og líkur á að tilraunin heppnist eru :math:`p = \lambda/n` í hvert skipti. Í skiladæmunum sönnuðuð þið að þegar :math:`n \to \infty` má lýsa fjölda koma með Poisson-dreifingu.

.. container:: center

   .. figure:: images/poisson_dreifing_4.svg
      :width: 367.75pt
      :align: center

Við minntumst líka á í Lík&töl að tíminn sem líður milli koma hefur veldisdreifingu með stika :math:`\lambda` þegar :math:`n` er stórt. Ef við keyrum þetta komulíkan endalaust og látum :math:`N(t)` vera fjölda koma yfir tímabilið :math:`[0,t]`, þá fæst svokallað **slembiferli** sem kallast Poisson-ferli með stika :math:`\lambda`.

Formlega má skilgreina Poisson-ferli með stika :math:`\lambda>0` þannig að tímarnir sem líða milli atburða séu óháðar veldisstærðir með stika :math:`\lambda`. Ef ferlið hefst á tíma :math:`0` er tíminn sem líður fram að fyrsta atburði :math:`S_1 = X_1`, tíminn sem líður fram að öðrum atburði er :math:`S_2 = X_1+X_2`, og svo koll af kolli, þar sem :math:`X_1,X_2,\ldots` eru óháðar veldisstærðir með stika :math:`\lambda`.

.. container:: center

   .. figure:: images/poisson_ferli_hermun.svg
      :width: 301.98pt
      :align: center

Í Poisson-ferli táknum við atburðatímana með :math:`S_1,S_2,\ldots` þar sem :math:`S_n = X_1+X_2+\cdots+X_n` fyrir :math:`n \geq 1`. Látum :math:`t \geq 0` og látum :math:`N(t)` tákna fjölda atburða sem gerast fram að tíma :math:`t`. Setjum :math:`S_0 := 0`. Þá má lýsa :math:`N(t)` svona:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    N(t) &= \max\{n \geq 0: S_n \leq t\}.
   \end{aligned}
   \]

Á myndinni að ofan er :math:`N(t)=4`. Við ætlum núna að herma Poisson-ferli og það verður síðan skoðað frekar í hermunarverkefninu. Poisson-ferli með stika :math:`\lambda` má herma svona yfir tímabilið :math:`[0,T]`:

   #. Setjum :math:`t=0` og :math:`n=0`. Breytan :math:`t` heldur utan um tímann sem hefur liðið og breytan :math:`n` heldur utan um fjölda atburða.

   #. Hermum tímann :math:`x` sem líður fram að næsta atburði, sem hefur veldisdreifingu með stika :math:`\lambda`.

   #. Setjum :math:`t \leftarrow t+x` til að uppfæra tímann sem hefur liðið.

   #. Ef :math:`t \leq T` setjum við :math:`n \leftarrow n+1`. Annars erum við komin út fyrir tímabilið :math:`[0,T]` og við hættum hermuninni.

   #. Endurtökum skref 2–4 eins oft og þarf.

   #. Þegar hermuninni er lokið er :math:`n` fjöldi atburða sem gerðist á tímabilinu :math:`[0,T]`.

Hægt er að sýna að í Poisson-ferli með stika :math:`\lambda` hefur fjöldi atburða sem gerist á tímabilinu :math:`[0,T]` Poisson-dreifingu með stika :math:`\lambda T`. Staðfestum þetta með því að herma Poisson-ferli.

.. rubric:: Hermun á Poisson-ferli

.. code-block:: r

   #Fall sem hermir Poisson-ferli N sinnum yfir tímabilið [0,T].
   #lambda er stiki Poisson-ferlisins.
   poisson_ferli_hermun <- function(N,lambda,T){
     #results_vec er vigur sem geymir hermdu gildin.
     results_vec <- c(1:N)
     #Hermum Poisson-ferli N sinnum yfir tímabilið [0,T].
     for (j in 1:N){
       #Byrjum á að núllstilla tímann (t) og fjölda atburða (n)
       t <- 0
       n <- 0
       #Breytan exit er notuð til að hætta hermuninni þegar það er viðeigandi.
       exit = 0
       while(exit == 0){
         #Hermum tímann sem líður fram að næsta atburði.
         x <- rexp(1,lambda)
         #Uppfærum tímann sem hefur liðið.
         t <- t + x
         #Athugum hvort við erum komin út fyrir endapunkt tímabilsins. 
         #Ef svo er hættum við, annars hækkum við fjölda atburða
         #á tímabilinu um einn og höldum áfram.
         if (t > T ){
           exit <- 1
         }
         else{
           n <- n+1 
         }
       }
       #Vistum hermdan fjölda atburða á tímabilinu [0,T].
       results_vec[j] <- n
     }

     #Skilum vigrinum með hermdu gildunum.
     return(results_vec)
   }

Búum síðan til fall sem tekur inn hermd gildi fyrir fjölda atburða á tímabilinu [0,T] og teiknar samanburðarmynd sem ber saman hlutfallstíðnir gildanna sem hermunin gefur og massafall Poisson-dreifingar með stika :math:`\lambda T`. Athugið að kóðinn er mjög svipaður og kóðarnir sem við notuðum að ofan fyrir Bernoulli- og tvíkostastærðirnar.

.. rubric:: Samanburður á hermdri hlutfallstíðni og massafalli Poisson-dreifingar

.. code-block:: r

   #Notum ggplot2 til að teikna.
   library(ggplot2)
   #Þessi valkostur sýnir tölur eins og 10^5 sem 100000.
   options(scipen=999)
   #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallstíðni
   #gilda í hermuninni við massafall Poisson-dreifingar með stika lambda*T.
   teikna_poisson_ferli <- function(results_vec,lambda,T){
     #Finnum stærsta gildið sem kom út úr hermuninni.
     max_gildi <- max(results_vec)
     #Reiknum hlutfallstíðni hermdu gildanna.
     tidnirit <- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
     #Búum til gagnasafn sem geymir gögnin fyrir hermdu hlutfallstíðnirnar.
     hlutfallstidni <- data.frame(
       x_gildi = 0:max_gildi,
       #tidnirit$density gefur hlutfallstíðnirnar
       y_gildi = tidnirit$density, 
       audkenni="Hermd hlutfallstíðni"
     )
     #Búum til gagnasafn sem geymir massafall Poisson-dreifingar með stika lambda*T.
     poisson_massafall <- data.frame(
       x_gildi = 0:max_gildi,
       y_gildi = dpois(0:max_gildi, lambda*T),
       audkenni="Massafall Poisson-dreifingar"
     )
     #Sameinum gagnasöfnin
     sameinud_gogn <- rbind(hlutfallstidni, poisson_massafall)
     ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
       #Teiknum stöplarit með geombar.
       geom_bar(stat = "identity", position = "dodge", alpha = 0.8) + 
       labs(title=paste("Niðurstöður fyrir lambda =",lambda,", T =",T," og N =",N), caption = paste("Samanburður á hermdri hlutfallstíðni fyrir fjölda atburða\nfram að tíma T =",T,"í Poisson-ferli með stika lambda =",lambda,"\nog massafalli Poisson-dreifingar með stika lambda*T =",lambda*T), x = "Gildi slembistærðarinnar", y ="") +
       scale_fill_manual(name="",values = c("Hermd hlutfallstíðni" = 'steelblue3', "Massafall Poisson-dreifingar" = 'brown3')) + 
       theme(plot.caption=element_text(size=11, hjust=0, face="italic", color="black"))
   }

.. rubric:: Gagnvirkur R-leikvöllur

.. raw:: html

   <div data-datacamp-exercise data-lang="r" data-height="600">
     <code data-type="pre-exercise-code">
       try(Sys.setlocale(&#39;LC_CTYPE&#39;, &#39;C.UTF-8&#39;), silent=TRUE)

       #Fall sem hermir Poisson-ferli N sinnum yfir t\u00EDmabili\u00F0 [0,T].
       #lambda er stiki Poisson-ferlisins.
       poisson_ferli_hermun &lt;- function(N,lambda,T){
         #results_vec er vigur sem geymir hermdu gildin.
         results_vec &lt;- c(1:N)
         #Hermum Poisson-ferli N sinnum yfir t\u00EDmabili\u00F0 [0,T].
         for (j in 1:N){
           #Byrjum \u00E1 a\u00F0 n\u00FAllstilla t\u00EDmann (t) og fj\u00F6lda atbur\u00F0a (n)
           t &lt;- 0
           n &lt;- 0
           #Breytan exit er notu\u00F0 til a\u00F0 h\u00E6tta hermuninni \u00FEegar \u00FEa\u00F0 er vi\u00F0eigandi.
           exit = 0
           while(exit == 0){
             #Hermum t\u00EDmann sem l\u00ED\u00F0ur fram a\u00F0 n\u00E6sta atbur\u00F0i.
             x &lt;- rexp(1,lambda)
             #Uppf\u00E6rum t\u00EDmann sem hefur li\u00F0i\u00F0.
             t &lt;- t + x
             #Athugum hvort vi\u00F0 erum komin \u00FAt fyrir endapunkt t\u00EDmabilsins. 
             #Ef svo er h\u00E6ttum vi\u00F0, annars h\u00E6kkum vi\u00F0 fj\u00F6lda atbur\u00F0a
             #\u00E1 t\u00EDmabilinu um einn og h\u00F6ldum \u00E1fram.
             if (t &gt; T ){
               exit &lt;- 1
             }
             else{
               n &lt;- n+1 
             }
           }
           #Vistum hermdan fj\u00F6lda atbur\u00F0a \u00E1 t\u00EDmabilinu [0,T].
           results_vec[j] &lt;- n
         }

         #Skilum vigrinum me\u00F0 hermdu gildunum.
         return(results_vec)
       }

       #Notum ggplot2 til a\u00F0 teikna.
       library(ggplot2)
       #\u00DEessi valkostur s\u00FDnir t\u00F6lur eins og 10^5 sem 100000.
       options(scipen=999)
       #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallst\u00ED\u00F0ni
       #gilda \u00ED hermuninni vi\u00F0 massafall Poisson-dreifingar me\u00F0 stika lambda*T.
       teikna_poisson_ferli &lt;- function(results_vec,lambda,T){
         #Finnum st\u00E6rsta gildi\u00F0 sem kom \u00FAt \u00FAr hermuninni.
         max_gildi &lt;- max(results_vec)
         #Reiknum hlutfallst\u00ED\u00F0ni hermdu gildanna.
         tidnirit &lt;- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
         #B\u00FAum til gagnasafn sem geymir g\u00F6gnin fyrir hermdu hlutfallst\u00ED\u00F0nirnar.
         hlutfallstidni &lt;- data.frame(
           x_gildi = 0:max_gildi,
           #tidnirit$density gefur hlutfallst\u00ED\u00F0nirnar
           y_gildi = tidnirit$density, 
           audkenni=&quot;Hermd hlutfallst\u00ED\u00F0ni&quot;
         )
         #B\u00FAum til gagnasafn sem geymir massafall Poisson-dreifingar me\u00F0 stika lambda*T.
         poisson_massafall &lt;- data.frame(
           x_gildi = 0:max_gildi,
           y_gildi = dpois(0:max_gildi, lambda*T),
           audkenni=&quot;Massafall Poisson-dreifingar&quot;
         )
         #Sameinum gagnas\u00F6fnin
         sameinud_gogn &lt;- rbind(hlutfallstidni, poisson_massafall)
         ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
           #Teiknum st\u00F6plarit me\u00F0 geombar.
           geom_bar(stat = &quot;identity&quot;, position = &quot;dodge&quot;, alpha = 0.8) + 
           labs(title=paste(&quot;Ni\u00F0urst\u00F6\u00F0ur fyrir lambda =&quot;,lambda,&quot;, T =&quot;,T,&quot; og N =&quot;,N), caption = paste(&quot;Samanbur\u00F0ur \u00E1 hermdri hlutfallst\u00ED\u00F0ni fyrir fj\u00F6lda atbur\u00F0a\nfram a\u00F0 t\u00EDma T =&quot;,T,&quot;\u00ED Poisson-ferli me\u00F0 stika lambda =&quot;,lambda,&quot;\nog massafalli Poisson-dreifingar me\u00F0 stika lambda*T =&quot;,lambda*T), x = &quot;Gildi slembist\u00E6r\u00F0arinnar&quot;, y =&quot;&quot;) +
           scale_fill_manual(name=&quot;&quot;,values = c(&quot;Hermd hlutfallst\u00ED\u00F0ni&quot; = &#39;steelblue3&#39;, &quot;Massafall Poisson-dreifingar&quot; = &#39;brown3&#39;)) + 
           theme(plot.caption=element_text(size=11, hjust=0, face=&quot;italic&quot;, color=&quot;black&quot;))
       }
     </code>
     <code data-type="sample-code">
       # Velji\u00F0 lambda, T og fj\u00F6lda hermana.
       N &lt;- 10000
       lambda &lt;- 3
       T &lt;- 5
       gildi &lt;- poisson_ferli_hermun(N, lambda, T)
       teikna_poisson_ferli(gildi, lambda, T)
     </code>
   </div>

Til gamans: Að reikna heildi með hermun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Segjum að við viljum reikna heildið

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \int_0^1 g(x) dx \qquad (\ast)
   \end{aligned}
   \]

fyrir eitthvert fall :math:`g: (0,1) \to \mathbb{R}`. Veljum óháðar tölur :math:`U_1,U_2,\ldots` af handahófi milli 0 og 1 og skilgreinum slembistærðirnar

.. math:: X_1 := g(U_1), \; X_2 := g(U_2), \; X_3 := g(U_3), \;\text{o.s.frv.}

Athugið að :math:`X_1,X_2,X_3,\ldots` eru óháðar slembistærðir sem hafa allar sömu dreifingu.

Setjum

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \bar{X}_n := \frac1n \sum_{i=1}^n X_i = \frac1n \sum_{i=1}^n g(U_i).
   \end{aligned}
   \]

Samkvæmt lögmáli mikils fjölda gildir að :math:`\bar{X}_n` nálgast :math:`\mathbb{E}[X_1] = \mathbb{E}[g(U_1)]` eftir því sem :math:`n` stækkar. En nú gildir skv. lögmáli ómeðvitaða tölfræðingsins að

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{E}[g(U_1)] &= \int_{-\infty}^\infty g(x) f(x) dx = \int_0^1 g(x) dx.
   \end{aligned}
   \]

Við getum þess vegna nálgað heildið í :math:`(\ast)` með því að velja tölur af handahófi milli 0 og 1, reikna fallgildi :math:`g` fyrir hverja og eina tölu, og taka meðaltal.

Segjum að við viljum reikna tvöfalda heildið

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \int_0^1 \int_0^1 g(x,y) dx dy \quad (\ast)
   \end{aligned}
   \]

fyrir eitthvert fall :math:`g: (0,1)^2 \to \mathbb{R}`. Veljum óháða punkta

.. math:: (U_1,V_1),(U_2,V_2),(U_3,V_3),\ldots

af handahófi úr einingakassanum og skilgreinum slembistærðirnar

.. math:: X_1 := g(U_1,V_1), \; X_2 := g(U_2,V_2), \; X_3 := g(U_3,V_3), \;\text{o.s.frv.}

Athugið að :math:`X_1,X_2,X_3,\ldots` eru óháðar slembistærðir sem hafa allar sömu dreifingu.

Setjum

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \bar{X}_n := \frac1n \sum_{i=1}^n X_i = \frac1n \sum_{i=1}^n g(U_i,V_i).
   \end{aligned}
   \]

Samkvæmt lögmáli mikils fjölda gildir að :math:`\bar{X}_n` nálgast :math:`\mathbb{E}[X_1] = \mathbb{E}[g(U_1,V_1)]` eftir því sem :math:`n` stækkar. En nú gildir skv. lögmáli ómeðvitaða tölfræðingsins að

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{E}[g(U_1,V_1)] &= \int_{-\infty}^\infty \int_{-\infty}^{\infty} g(x,y) f(x,y) dx dy \\ &= \int_0^1 \int_0^1 g(x,y) dx dy.
   \end{aligned}
   \]

Við getum þess vegna reiknað tvöfalda heildið í :math:`(\ast)` með því að velja punkta af handahófi úr einingakassanum, reikna falligildi :math:`g` í punktunum, og taka meðaltal.

Hermun er ekki endilega fljótlegasta leiðin til að reikna ein- og tvívíð heildi, en hún getur orðið gagnleg þegar reikna þarf yfir tugi eða hundruði vídda, sem kemur t.d. fyrir þegar verið er að greina flókin gagnasöfn.
