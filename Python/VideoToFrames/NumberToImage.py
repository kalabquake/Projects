from PIL import Image

# The number to convert to image
number = 992612939891620037098810843442624403049635674266739232679881053746191996136937906742094779634863085125012321378783984827157109215620413106828570082252212130015065466462206238845548357621464664885493339207688454230038155238254637858984334954399439681802022008112583527285729611061945699441221907508499086030306042733269027356168681484461892154969771645878322202568275540780140603957645156342511826074602061703222213545997732084345195499019206115549365630852684276997996041777747103946445182695466880465239304720542634699008984737394276470005332069250549252965864373902788752951489683645761109029205559542161567024162722528446728337159021553573258500992815516445353976555112944137383360724515867045161509986749346907362604926029289749735959179792769782640118654656764893947730975389095330987351332522726386829981864685894030046334677110990380454745575246715135757613855248705591768136724344015571350709948089035396698727498414672601845349330179631845014709855207306625469400433128734913697517257478645185034666221695790235828255595120942722309367286692182171805413919237715157959443482311349696782331710755599198765930453170217977427111881144960530936876048122055415544394390584099418165318805161101676642701648296445948532616225581399881022831709865650541206985144707212995524207779689649649499782243314749293428334379817553723351584567231996219738212214354385854203525006212285579788307581798768848027146410007309705622310022907932740646751657448087461586463388037710095989988984720049998240601528078482849071694227458243432977137323850582472117579723376656283987620970304308823651377353473209934817924131692229052784425320855717216571606350673677575577964591820539044440060127452261035397139983113871732621852246315360973827160632875796812329497920014681739557207246429706306027178477209660972537800600368726400437719872289990110985280702792619746010518150020578479280977950858427460010388912033215741160713949135484453971636612984262653118474448687229855303289645124861707058376472309197560217177905635615222636183991383448678501866474009907788522443346162874862989195439043356163974983397230141005224969771198154208760747467578450074575695360359505515093598646313838174646758343679443712913718087625155972232772158992622959173684667688470620489876985860367699211016246082760330471093311865033540244396591207000988006770617008917166206299227325722206582497232723912181733381142376039430716541037209081609235869215754435415684902059998192327404880063196191408966800833626645276381644820206624131815632615625343317473382309335362812380806171272180981686440480848595978281952226257429864593671553426355274622375409344651736905274144171300360145007625299394605873054428215699858065115218369123199580743371952850881285093810319214956589494542874932922829005513412459976507483293718468203200462081199220105707092863862176921258085164897854358296706498699121369466152667642383970902843557847225591174837813583582962684919084773814198296425308378999253656405091432748449198811291191450009091886604433113392670004804370374628611008218484373860452892767392213157550184657656133992669338191593944135304358402880129843502833994763930367338470163807047284879200859638001999672630032486281020140662599757715929445733824018936326403446507604720369457474426537888277549628849330069637371762960678923130432143454920046147949679392459468093600360941622204685722237566483683186016043482012591268164236503140022802618763718179639303697558079168201347981787637112197878565595582293478871169443754818703648444381472860235133768245031498677762840650062344184879478035225900367307141947745295695726822429656404420286154115058234678941945127812725589472107886261884503247788192466410107834488685483202594051783157501461230523830520868226965944101932742857617120803802572951415732386258302535025126645714073101763421614783747498324794248876410366644099507408884623595995626662116675304462644041674726326252549713977475825920812641803322361921577109368505507046417991394353681639536395967183786729272436305933896544218628417413182991627853097605579654900159890392055083944152625886344633189606620814897579259255621872636060220881996872536611023841620624353221626328221174220836605314401787996467316262014762642081890307642224003330075227320582123020664478687722643807194027881962352618373177333739209665222146636745832392873790331107063641904122468941876919868352924789436220193932328734424123554167171762575060408626392860568021621359759374965931062851509824089431835590885399538828178735020075459990306792792254168183456405988484937352568620266281376523332802729109604309833832002174773224085126260392393587457036923799753841946456544410942139587868730303081586736645663757232307264400306457896538104590889295920481420659864472582565506966675779933350171663572638273438521356744965692079444179227226238411371345651224514044119543029973869522382765908617327075328874758581446722671796353390210030480481854575916971664644441910982594106396163235510933482131084606682012235622862844552597809936564752006368540379809288033991161224938954006393316638315569236031760925915999054359612211238041933003715828365113881163476855268582828232779114941311344470685587325114777848171862576984206814950239274447269962774963253820208000399014829291270688461384518566306207394589010491999372088108646963245341007684701227703095021389415178300745192725006977419769871591358019871121764374078982577437975992812620341285284322953457224214292988112425891164048047280238629020355721083338852602071095583017335526311062472291889422712841024727386334032184369064478978766643657350022396781561560722867362648163934672896919200311955338631312966940690466302461623989819786368269405390173643141758111364130483589249121262309915884311097235142424240086769752360424855258336586711272492767542400598492085045283700935369383884972085904627787392652726115315930051497309653668854181677019434348610957442326711680516600443972855215473872077678423171616448731259954973143183465697193139153224917862297525669598711899340173363970936146826152078554688615930720075339251503014290651924459555191133200441003433766005513304664354981334065260225620012826859078659716850135703815700258741327457617191132078377906963882025258798252726445369698588594107504720948162474580243011995088591455820733108376849064144994369250907806491805551039638255517637237187899764887295022068298277289364726400174758874637601522808191364369097278479203772837361448183685357656068150886077578460006481296533524865959768020364281755637122321745051866905788277847017221706591796918046826375983394680573058315779550574475124630398065429218796793864076502001513785062857501724595184537553848190841622050167696873936474024532113160969020547294998217210663279832408705912414788031603253559912077191427802664197900418977293441789718944120004394496645222991197910621149815567523080333932861249456587386914577384987847778387996050970532192754737096225249265388847788999852351900387516991931756635670799167358818432711570345680035347629571240198310548836745186441228246463974005087587380660450396900926059371616839034272767646372788608134171957395712913039336514696878843929626464196985815673934926650400981016420181473715568066121219396540151380627289123891028789344229401174192965302068086526492652690988211054209627543099719152931393648340645911159743557563751013078835851036824778161070930743249475940694635946227311331041049024521359827743606022673345149152428526362516440045412621104456105810121370397941169500422981372796670303193113591824995921705395734097113396893031752570137552500453341149330516053835634751019398173421575238040216837093103822655247828810308534315710150133657152552906311384835161367973098013201071911496585573163703787325189584895539823048303795197174925775382989179587525088499312219226706662938285085733399722941041125056444079208387981549633391666108608755338624663000100550425125367622527648363309966726133226714438776472428757620190796651438917760091291550657382750905660404689769691687178508229308992772785297845096094340717539034409331397860450920471241765300938570911577732813283876573436988191191437229602338483956537602294600976986728793080172227795792538564956193974280627536459191722096163715881169919312956959826715892060615195376000015641228391076470523908107820782056094892052327187886931228485966238513715758794964415207138223308893808559963200478247653361135092883330429702158526225771793701278030307102342719697956845161489463723037855979812951062767259663735317816455849286697378862421469076742921138606174174360834711507081741895316366611219398717025885103091880216841450610638854713592244136558826532418272495353212341611229654645547155406418280086690758300339779625036654744014925123168376755100578769906110088693320030140655201029893547696457574794870796301542780357635109683556859378584251110555911742794454200545365370722001846016705165087029703229344396557545047149583458936625234514644999954951340434097953140601224184074758653231849658990600874281412435518481415554244363033677499615855673735604208889349637487427091636716544895993899728890061976136112948477543323795448

# Get the image width and height from the number of bits
width = 200
height = 150

# Create a new image with the calculated width and height
image = Image.new("1", (width, height), 0)

# Iterate over the bits in the number
for i in range(width*height):
    # Check if the bit at position i is set
    if number & (2**i):
        # If it is, set the corresponding pixel in the image
        x = i % width
        y = i // width
        image.putpixel((x, y), 1)

# Display the image
image.show()