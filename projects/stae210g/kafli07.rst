Poisson-ferli og Gamma-dreifingin
=================================

Skilgreining á Poisson-ferli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við kynntum Poisson-ferli óformlega til sögunnar í Lík&töl. Poisson-ferli lýsir streymi atburða, t.d. fjölda koma á bráðamóttökuna eða fjölda bíla sem fara framhjá ákveðnum punkti á þjóðveginum, sem er þannig að í mesta lagi einn atburður verði yfir hvert stutt tímabil, litlar líkur séu á atburði á hverju stuttu tímabil, og atburðir séu óháðir milli tímabila. Poisson-ferli má óformlega smíða með því að kasta krónum. Við skiptum þá tímaásnum niður í stutt tímabil og köstum krónu á hverju tímabili til að ákvarða hvort atburður gerist á tímabilinu eða ekki, á þann veg að útkomur krónukastanna séu óháðar milli tímabila.

Poisson-ferli með stika :math:`\lambda>0` má formlega skilgreina þannig að tímarnir sem líða milli atburða séu óháðar veldisstærðir með stika :math:`\lambda`. Við sjáum líka í umfjöllun okkar um hermun að ef Poisson-ferli er skilgreint þannig, þá hefur fjöldi atburða sem gerist á tímabilinu :math:`[0,T]` Poisson-dreifingu með stika :math:`\lambda T`. Munum að slembistærð :math:`Y` sem hefur Poisson-dreifingu með stika :math:`\mu>0` hefur líkindafall

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(Y=k) = e^{-\mu} \frac{\mu^k}{k!}, \quad k=0,1,2,\ldots.
   \end{aligned}
   \]

Við ætlum nú að setja Poisson-ferli fram á skipulegri hátt og lýsa helstu eiginleikum þess. Fyrst kynnum við til sögunnar helstu hugtökin á mynd.

.. container:: center

   .. figure:: images/poisson_ferli_hermun.svg
      :width: 301.98pt
      :align: center

Látum :math:`X_1,X_2,\ldots` vera óháðar veldisstærðir með stika :math:`\lambda>0`. Poisson-ferli er skilgreint þannig að tíminn sem líður fram að fyrsta atburði er :math:`S_1 = X_1`, tíminn sem líður fram að öðrum atburði er :math:`S_2 = X_1+X_2`, og svo koll af kolli. Almennt eru atburðatímarnir táknaðir með :math:`S_1,S_2,\ldots`, þar sem :math:`S_n = X_1+X_2+\cdots+X_n` fyrir :math:`n \geq 1` er tíminn sem :math:`n`-ti atburðurinn gerist á. :math:`X_1,X_2,\ldots` eru tímarnir sem líða milli atburða. Fjölda atburða sem gerist fram að tíma :math:`t` má lýsa svona:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    N(t) &= \max\{n \geq 0: S_n \leq t\}.
   \end{aligned}
   \]

Á myndinni að ofan er til dæmis :math:`N(t)=4`. Setjum nú skilgreininguna formlega fram.

.. admonition:: Skilgreining 15.
   :class: box-definition

   Látum :math:`X_1,X_2,\ldots` vera óháðar veldisstærðir með stika :math:`\lambda>0`. Setjum :math:`S_0 := 0` og skilgreinum fyrir sérhvert :math:`n \geq 1`:

   .. math:: S_n := X_1 + X_2 + \cdots +X_n.

   Skilgreinum jafnframt fyrir sérhvert :math:`t \geq 0`:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              N(t) :=  \max\{n \geq 0: S_n \leq t\}.
      \end{aligned}
      \]

   Safnið :math:`\big(N(t)\big)_{t \geq 0}` af slembistærðunum :math:`N(t)` fyrir :math:`t \geq 0` kallast Poisson-ferli með stika :math:`\lambda`. Slembistærðirnar :math:`S_1,S_2,\ldots` kallast **atburðatímar** ferlisins og slembistærðin :math:`N(t)` er túlkuð sem fjöldi atburða sem gerist fram að tíma :math:`t`.

Munum að veldisstærð :math:`X` með stika :math:`\lambda>0` er **minnislaus**, sem þýðir að fyrir sérhverjar rauntölur :math:`a,b \geq 0` gildir að

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(X>a+b \,|\, X>a) = \mathbb{P}(X>b).
   \end{aligned}
   \]

Ef við segjum að :math:`X` lýsi endingartíma tækis, þá þýðir minnisleysið að alltaf þegar við spyrjum hverjar líkurnar eru á að tækið endist ákveðinn tíma til viðbótar, þá eru líkurnar óháðar aldri tækisins á þeim tíma sem við spyrjum.

Minnisleysi veldisstærðarinnar einfaldar mjög greiningu á Poisson-ferlum, en minnisleysið leiðir líka til hegðunar sem virðist oft skrítin þegar fljótt er á litið. Sem dæmi: Ef við göngum inn í Poisson-ferli með stika :math:`\lambda>0`, þá hefur tíminn sem líður fram að næsta atburði veldisdreifingu með stika :math:`\lambda`, sama hversu langt er síðan síðasti atburður gerðist. Þetta hefur í för með sér að bilið sem við göngum inn í er lengra en bil sem valið er af handahófi (raunar er það tvöfalt lengra). Þetta er oft kallað ,,skoðunarþversögnin“, sem nánar er fjallað um í hermunarverkefninu.

Helstu eiginleikar Poisson-ferlis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 20.
   :class: box-theorem

   Látum :math:`\big(N(t)\big)_{t \geq 0}` vera Poisson-ferli með stika :math:`\lambda`.

   (1) Fyrir sérhvert :math:`n \geq 1` og :math:`0 < t_1 < t_2 < \cdots < t_n` gildir að

       .. math:: N(t_1), N(t_2)-N(t_1), \ldots, N(t_n)-N(t_{n-1})

       eru óháðar slembistærðir.

   (2) Setjum :math:`t_0:=0`. Fyrir sérhvert :math:`i=1,\ldots,n` hefur slembistærðin :math:`N(t_i)-N(t_{i-1})` Poisson-dreifingu með stika :math:`\mu_i := \lambda (t_i-t_{i-1})`. Þetta þýðir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                      \mathbb{P}\big(N(t_i)-N(t_{i-1}) = k\big) &=  e^{-\mu_i} \frac{\left(\mu_i\right)^k}{k!} \\
                      &= e^{-\lambda (t_i-t_{i-1})} \frac{\big(\lambda (t_i-t_{i-1})\big)^k}{k!}
          \end{aligned}
          \]

       fyrir sérhvert :math:`k=0,1,2,\ldots`.

   (3) Látum :math:`n \geq 1`, látum :math:`U_1,U_2,\ldots,U_n` vera óháðar slembistærðir með jafna dreifingu á bilinu :math:`[0,T]` og látum :math:`U_{(1)},\ldots,U_{(n)}` tákna sömu stærðir eftir að þeim hefur verið raðað í (vaxandi) stærðarröð. Ef skilyrt er með :math:`\{N(T)=n\}`, þá hafa atburðatímarnir :math:`S_1,S_2,\ldots,S_n` sömu dreifingu og :math:`U_{(1)},\ldots,U_{(n)}`.

.. admonition:: Athugasemd.
   :class: box-remark

   Þar sem :math:`N(t_i)` er fjöldi atburða sem gerist fram að tíma :math:`t_i`, þá er :math:`N(t_i)-N(t_{i-1})` einfaldlega fjöldi atburða sem gerist á tímabilinu :math:`(t_{i-1},t_i]` fyrir :math:`i=1,\ldots,n`. Athugum að ef við setjum :math:`t_0 := 0`, þá er :math:`N(t_1)-N(t_0) = N(t_1)`.

   .. container:: center

      .. figure:: images/poisson_independent_increments.svg
         :width: 378.37pt
         :align: center

   | Liður (1) í Setningu 20 segir óformlega að fjöldi atburða sem gerist á tilteknu tímabili er óháður fjölda atburða sem gerist á öðrum tímabilum. Þetta er mjög eðlilegt ef við hugsum Poisson-ferli þannig að óháðum krónum sé kastað til að ákvarða hvenær atburðir gerast. Einnig er þetta afleiðing af minnisleysi veldisstærðarinnar, sem við fjölluðum um í Fyrirlestri 3. Liður (2) segir að fjöldi atburða á tímabilinu :math:`(t_{i-1},t_i]` hafi Poisson-dreifingu með stika sem er í réttu hlutfalli við lengd tímabilsins. Aftur er eðlilegt að fjöldi atburða sem gerist á tilteknu tímabili sé háður lengd tímabilsins.
   | Liðir (3) í Setningu 20 að ef við vitum að :math:`n` atburðir gerast fram að tíma :math:`T` í Poisson-ferli, þá má fá atburðatímana :math:`S_1,S_2,\ldots,S_n` með því að velja :math:`n` punkta af handahófi milli :math:`0` og :math:`T` og láta :math:`S_1` vera lægsta punktinn, :math:`S_2` næstlægsta punktinn, og svo koll af kolli. Ef við vitum fjölda atburða á tímabilinu :math:`[0,T]` er þess vegna enginn hluti tímabilsins líklegri til að innihalda atburð en einhver annar hluti þess. Þetta er aftur eðlilegt ef við höfum í huga að Poisson-ferli má hugsa þannig að óháðum krónum sé kastað til að ákvarða hvenær atburðirnir gerast.

Gamma-dreifingin
~~~~~~~~~~~~~~~~

Tíminn sem líður fram að :math:`n`-ta atburði í Poisson-ferli er gefinn með

.. math::
   :nowrap:

   \[
   \begin{aligned}
       S_n = X_1+X_2+\cdots+X_n
   \end{aligned}
   \]

þar sem :math:`X_1,X_2,\ldots,X_n` eru óháðar veldisstærðir með sama stikann :math:`\lambda`. Í hermunarverkefninu sýnum við að stærðin :math:`S_n` hefur svokallaða *Gamma-dreifingu* með stika :math:`n` og :math:`\lambda`, sem er samfelld dreifing með þéttleikann

.. math::
   :nowrap:

   \[
   \begin{aligned}
           f(x) = \begin{cases}
               \dfrac{\lambda^n}{(n-1)!} x^{n-1} e^{-\lambda x}, & x \geq 0, \\ 0, & x<0.
           \end{cases}
   \end{aligned}
   \]



Þegar :math:`n=1` fæst þéttleikinn

.. math::
   :nowrap:

   \[
   \begin{aligned}
           f(x) = \begin{cases}
               {\lambda} e^{-\lambda x}, & x \geq 0, \\ 0, & x<0.
           \end{cases}
   \end{aligned}
   \]

sem er þéttleiki veldisdreifingar. Þar sem væntigildi er línulegt gildir að

.. math:: E[S_n] = \mathbb{E}[X_1]+\mathbb{E}[X_2] + \cdots + \mathbb{E}[X_n] = n/\lambda.


