import textwrap

list1 = ["Adamant", "Adanedhel", "Adûnakhôr", "Adûnaic", "Adurant", "Aeglos", "Aegnor", "Aelin-uial", "Aerandir", "Aerin", "Aftercomers", "Agarwaen", "Aglarond", "Aglon", "Ainulindalë", "Ainur", "Akallabêth",
         "Alcarinquë", "Aldaron","Aldudénië", "Almaren", "Alqualondë", "Aman", "Amandil", "Amanyar", "Amarië", "Amlach", "Amon Amarth", "Amon Ereb", "Amon Ethir", "Amon Gwareth", "Amon Obel",
         "Amon Rûdh", "Amon Sûl", "Amon Uilos", "Amras", "Amrod", "Anach", "Anadûnë", "Anar", "Anárion", "Anarríma", "Ancalagon", "Andor", "Andram", "Androth", "Anduin", "Andúnië",
         "Anfauglir", "Anfauglith", "Angainor", "Angband", "Anghabar", "Anglachel", "Angrenost", "Angrim", "Angrist", "Angrod", "Anguirel", "Annael", "Annatar", "Annon-in-Gelydh",
         "Annúminas", "Anor", "Apanónar", "Aradan", "Aragorn", "Araman", "Aranel", "Aranrúth", "Aranwë", "Aratan", "Aratar", "Arathorn", "Arda", "Ard-galen", "Aredhel",
         "Ar-Feiniel", "Ar-Gimilzôr", "Argonath", "Arien", "Armenelos", "Arnor", "Aros", "Arossiach", "Ar-Pharazôn", "Ar-Sakalthôr", "Arthad", "Arvernien", "Ar-Zimraphel",
         "Ascar", "Astaldo", "Atalantë", "Atanamir", "Atanatári", "Atani", "Aulë", "Avallónë", "Avari", "Avathar", "Azaghâl", "Balan", "Balar", "Balrog", "Barad-dûr",
         "Barad Eithel", "Barad Nimras", "Baragund", "Barahir", "Baran", "Baranduin", "Bar-en-Danwedh", "Battles of Beleriand", "Bauglir", "Beleg", "Belegaer", "Belegost", "Belegund",
         "Beleriand", "Belfalas", "Belthil", "Belthronding ", "Bëor", "Bereg", "Beren", "Black Land", "Black Sword", "Black Years", "Blessed Realm", "Blue Mountains", "Bor", "Borlach",
         "Borlad", "Boromir ", "Boron", "Borosaith ", "Borthand", "Bragollach", "Brandir", "Bregolas", "Bregor", "Brethil", "Bridge of Esgalduin", "Brilthor", "Brithiach", "Brithombar", "Brithon", "Brodda",
         "Cabed-en-Aras", "Cabed Naeramarth", "Calacirya", "Calaquendi", "Calenardhon", "Camlost", "Caragdûr", "Caranthir", "Carcharoth", "Cardolan", "Carnil", "Celeborn (1)", "Celeborn (2)",
         "Celebrant", "Celebrimbor", "Celebrindal", "Celebros", "Celegorm", "Celon", "Children of Ilúvatar", "Círdan", "Cirith Ninniach", "Cirith Thoronath", "Cirth", "Ciryon", "Corollaírë",
         "Crissaegrim", "Crossings of Teiglin", "Cuiviénen", "Culúrien", "Curufin", "Curufinwë", "Curunír", "Cúthalion", "Daeron", "Dagnir", "Dagnir Glaurunga", "Dagor Aglareb", "Dagor Bragollach",
         "Dagorlad", "Dagor-nuin-Giliath", "Dairuin", "Dark Elves", "Dark Lord", "Day of Flight", "Deathless Lands", "Deldúwath", "Denethor", "Dimbar", "Dimrost", "Dior", "Dispossessed",
         "Del Guldur", "Dolmed", "Dor Caranthir", "Dor-Cúarthol", "Dor Daedeloth", "Dor Dínen", "Dor Firn-i-Guinar", "Doriath", "Dorlas", "Dor-lómin", "Dor-nu-Fauglith", "Dorthonion",
         "Dragon-helm of Dor-lómin", "Dragons", "Draugluin", "Drengist", "Dry River", "Duilwen", "Dúnedain", "Dungartheb", "Durin", "Dwarf-road", "Dwarrowdelf", "Dwarves", "Petty-Dwarves",
         "Seven Fathers of the Dwarves", "Nauglamír", "Naugrim", "Eä", "Eagles", "Eärendil", "Eärendur (1)", "Eärendur (2)", "Eärnil", "Eärnur", "Eärrámë", "Eärwen", "Easterlings",
         "Echoing Mountains", "Echoriath", "Echtelion", "Edain", "Edrahil", "Eglador", "Eglarest", "Eglath", "Eilinel", "Eithel Ivrin", "Eithel Sirion", "Ekkaia", "Elbereth", "Eldalië",
         "Eldamar", "Eldar", "Eldarin", "Elder Days", "Elder King", "Eledhwen", "Elemmírë (1)", "Elemmírë (2)", "Elendë", "Elendil", "Elendili", "Elendur", "Elenna", "Elentári", "Elenwë", "Elerrína",
         "Elf-friends", "Elostirion", "Elrond", "Elu", "Eluchíl", "Eluréd", "Elurín", "Elvenhome", "Elves", "Elwë", "Elwing", "Emeldir", "Emyn Beraid", "Enchanted Isles", "Encircling Mountains",
         "Encircling Sea", "Endor", "Engwar", "Eöl", "Eönwë", "Ephel Brandir", "Ephel Dúath", "Erchamion", "Erech", "Ered Engrin", "Ered Gorgoroth", "Ered Lindon", "Ered Lómin", "Ered Luin",
         "Ered Nimrais", "Ered Wethrin", "Eregion", "Ereinion", "Erellont", "Eressëa", "Eriador", "Eru", "Esgalduin", "Estë", "Estolad", "Ezellohar", "Faelivrin", "Faithful, The", "Falas", "Falathar",
         "Falathrim", "Falmari", "Faramir", "Fëanor", "Fëanturi", "Felagund", "Finarfin", "Finduilas", "Fingolfin", "Fingon", "Finrod", "Finwë", "Fírimar", "Firstborn, The", "Followers, The", "Ford of Stones",
         "Fords of Aros", "Formenos", "Fornost", "Forsaken Elves", "Frodo", "Fuinur", "Gabilgathol", "Galadriel", "Galathilion", "Galdor", "Gandalf", "Gates of Summer", "Gelion", "Gelmir (I)", "Gelmir (2)",
         "Gildor", "Gil-Estel", "Gil-galad", "Gimilkhâd", "Gimilzôr",  "Ar-Gimilzôr", "Gimli", "Ginglith", "Gladden Fields", "Glaurung", "Glingal", "Glirhuin", "Glóredhel", "Glorfindel", "Golodhrim", "Gondolin",
         "Gondolindrim", "Gondor", "Gonnhirrim", "Gorgoroth (1)", "Gorgoroth (2)", "Gorlim", "Gorthaur", "Gorthol", "Gothmog", "Greater Gelion", "Great Lands", "Great River", "Green-elves", "Greenwood the Great",
         "Grey-elven tongue", "Grey-elves", "Grey Havens", "Greymantle", "Grinding Ice", "Grond", "Guarded Plain", "Guarded Realm", "Guilin", "Gundor", "Gurthang", "Gwaith-i-Mírdain", "GGwindor",
         "Hadhodrond", "Hador", "Haladin", "Haldad", "Haldan", "Haldar", "Haldir", "Haleth", "Half-elven", "Halflings", "Halls of Awaiting", "Halmir", "Handir", "Haradrim", "Hareth", "Hathaldir", "Hathol",
         "Haudh-en-Arwen", "Haudh-en-Elleth", "Haudh-en-Ndengin", "Haudh-en-Nirnaeth", "Havens, The", "Helcar", "Helcaraxë", "Helevorn", "Helluin", "Herumor", "Herunúmen", "Hidden Kingdom", "High-elven",
         "High Elves", "High Faroth", "Hildor", "Hildórien", "Himlad", "Himring", "Hírilorn", "Hísilómë", "Hithaeglir", "Hither Lands", "Hithlum", "Hollin", "Hollowbold", "Huan", "Hunthor", "Huor",
         "Húrin", "Hyarmentir", "Iant Iaur", "Ibun", "Idril", "Illuin", "Ilmarë", "Ilmen", "Ilúvatar", "Imlach", "Imladris", "Indis", "Ingwë", "Inziladûn", "Inzilbêth", "Irmo", "Iron Mountains",
         "Isengard", "Isil", "Isildur", "Istari", "Ivrin", "Karkaras", "kelvar", "Kementári", "Khazâd", "Khazad-dûm", "Khîm", "King's Men", "Kinslaying, The", "Ladros", "Laer Cú Beleg", "Laiquendi", "Lalaith", "Lammoth",
         "Land of Shadow", "Land of the Dead that Live", "Land of the Star", "Lanthir Lamath", "Last Alliance", "Laurelin", "Lay of Leithian", "Legolas", "Legolin", "lembas", "Lenwë", "Lhûn", "Linaewen",
         "Lindon", "Lindórië", "Little Gelion", "Loeg Ningloron", "lómelindi", "Lómion", "Lonely Isle", "Lord of Waters", "Lords of the West", "Lorellin", "Lorgan", "Lórien (1)", "Lórien (2)", "Lórindol",
         "Losgar", "Lothlann", "Lothlórien", "Luinil", "Lumbar", "Lúthien", "Mablung", "Maedhros", "Maeglin", "Maglor", "Maglor's Gap", "Magor", "Mahal", "Máhanaxar", "Mahtan", "Maiar", "Maiarin", "Malach",
         "Malduin", "Malinalda", "Mandos", "Manwë", "Marach", "March of Maedhros", "Mardil", "Mar-nu-Falmar", "Melian", "Melkor", "Men", "Menegroth", "Meneldil", "Menelmacar", "Meneltarma", "Meres of Twilight",
         "Mereth Aderthad", "Mickleburg", "Middle-earth", "Mîm", "Minas Anor", "Minas Ithil", "Minas Morgul", "Minastir", "Minas Tirith (1)", "Minas Tirith (2)", "Mindeb", "Mindolluin", "Mindon Eldalieva", "Míriel (1)",
         "Míriel (2)", "Mirkwood", "Misty Mountains", "Mithlond", "Mithrandir", "Mithrim", "Mordor", "Morgoth", "Morgul", "Moria", "Moriquendi", "Mormegil", "Morwen", "Mountain of Fire", "Mountains", "Mount Doom",
         "Music of the Ainur", "Nahar", "Námo", "Nandor", "Nan Dungortheb", "Nan Elmoth", "Nan-tathren", "Nargothrond", "Narn i Hîn Húrin", "Narog", "Narsil", "Narsilion", "Narya", "Nauglamír", "Naugrim", "Nazgûl",
         "Necklace of the Dwarves", "Neithan", "Neldoreth", "Nénar", "Nen Girith", "Nenning", "Nenuial", "Nenya", "Nerdanel", "Nessa", "Nevrast", "Nienna", "Nienor", "Nimbrethil", "Nimloth (1)", "Nimloth (2)",
         "Nimphelos", "Níniel", "Ninquelótë", "niphredil", "Nirnaeth Arnoediad", "Nivrim", "Noegyth Nibin", "Nogrod", "Noldolantë", "Noldor", "Nóm, Nómin", "North Downs", "Nulukkizdîn", "Númenor", "Númenóreans",
         "Nurtalë Valinóreva", "Ohtar", "Oiolossë", "Oiomúrë", "Olórin", "olvar", "Olwë", "Ondolindë", "Orcs", "Orfalch Echor", "Ormal", "Orocarni", "Orodreth", "Orodruin", "Oromë", "Oromët", "Orthanc", "Osgiliath",
         "Ossë", "Ossiriand", "Ost-in-Edhil", "Outer Lands", "Outer Sea", "Palantíri", "Pelargir", "Pelóri", "People of Haleth", "Periannath", "Petty-dwarves", "Pharazôn", "Prophecy of the North", "Quendi",
         "Quenta Silmarillion", "Quenya", "Radagast", "Radhruin", "Ragnor", "Ramdal", "Rána", "Rathlóriel", "Rauros", "Red Ring, The", "Region", "Rerir", "Rhovanion", "Rhudaur", "Rían", "Ringil", "Ring of Doom",
         "Rings of Power", "Ringwil", "Ring-wraiths", "Rivendell", "Rivil", "Rochallor", "Rohan", "Rohirrim", "Romenna", "Rothinzil", "Rúmil", "Saeros", "Salmar", "Sarn Athrad", "Saruman", "Sauron", "Secondborn, The",
         "Seeing Stones", "Serech", "seregon", "Serindë", "Seven Fathers of the Dwarves", "Seven Stones", "Shadowy Mountains", "Shepherds of the Trees", "Shelob", "Sickle of the Valor", "Silmarien", "Silmarils", "Silpion",
         "Silvan Elves", "Sindar", "Sindarin", "Singollo", "Sirion", "Sons of Fëanor", "Soronúmë", "Stone of the Hapless", "Straight Road, Straight Way", "Strongbow", "Súlimo", "Swanhaven", "Swarthy Men", "Talath Dirnen",
         "Talath Rhunen", "Taniquetil", "Tar-Ancalimon", "Taras", "Tar-Atanamir", "Tar-Calion", "Tar-Ciryatan", "Tar-Elendil", "Tar-Minastir", "Tar-Minyatur", "Tar-Míriel", "Tarn Aeluin", "Tar-Palantir", "Taur-en-Faroth",
         "Taur-im-Duinath", "Taur-nu-Fuin", "Tauron", "Teiglin", "Telchar", "Telemnar", "Teleri", "Telperion", "Telumendil", "Thalion", "Thalos", "Thangorodrim", "Thargelion", "Thingol", "Thorondor", "Thousand Caves",
         "Thranduil", "ThurIngwëthil", "Tilion", "Tintallë", "Tinúviel", "Tirion", "Tol Eressëa", "Tol Galen", "Tol-in-Gaurhoth", "Tol Morwen", "Tol Sirion", "Tulkas", "Tumhalad", "Tumladen", "Tumunzahar", "Túna",
         "Tuor", "Turambar", "Turgon", "Tûr Haretha", "Túrin", "Twilight Meres", "Two Kindreds", "Two Trees of Valinor", "Uinen", "Úlairi", "Uldor", "Ulfang", "Ulfast", "Ulmo", "Ulumúri", "Ulwarth", "Úmanyar",
         "Úmarth", "Umbar", "Undying Lands", "Ungoliant", "Union of Maedhros", "Urthel", "Urulóki", "Utumno", "Vairë", "Valacirca", "Valandil", "Valaquenta", "Valar", "Valaraukar", "Valarauko", "Valaróma", "Valie", "Valier", "Valimar",
         "Valinor", "Valmar", "Vána", "Vanyar", "Varda", "Vása", "Vilya", "Vingilot", "Vinyamar", "Voronwë", "Westernesse", "White Council", "White Mountain", "White Tree", "Wildman of the Woods", "Wilwarin", "Wingilótë",
          "Wizards", "Woodland Elves", "Yavanna", "Year of Lamentation"

          ]

descriptions = [
    "One of the Three Rings of the Elves, the Ring of Water, borne by Galadriel; also called the Ring of Nenya.",
    "'Elf-Man', name given to Túrin in Nargothrond.",
    "'Lord of the West', name taken by the nineteenth King of Númenor, the first to do so in the Adûnaic(Númenórean) tongue; his name in Quenya was Herunúmen.",
    "'Language of the West' or the native name Adûnayân, was the Númenórean language, spoken by the Men of Númenor during the Second Age.",
    "The sixth and most southerly of the tributaries of Gelion in Ossiriand. The name means 'double stream', referring to its divided course about the island of Tol Galen."
]



while True:
    print("Please choose an item to learn more about:")
    for i, item in enumerate(list1, start=1):
        print(f"{i}. {item}")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice.isnumeric() and 1 <= int(choice) <= len(list1):
            break
        else:
            print("Invalid choice. Please enter a number between 1 and", len(list1))

    index = int(choice) - 1
    item = list1[index]
    description = descriptions[index]
    wrapped_description = textwrap.fill(description, width=60)
    print(f"\n{item}: {description}")

    while True:
        more_info = input(f"Do you want more information about the meaning of {item}? (yes or no): ")
        if more_info.lower() in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if more_info.lower() == 'yes':
        if item == 'Adamant':
            print(
                "Adamant was a mythical stone of impenetrable hardness. It was often referred to with diamond features. It has no real relation with Tolkien's works other than occasional mentions to describe the Silmarils and a reference to Nenya, "
                "one of the rings of power held by Galadriel, as the Ring of Adamant.")
        elif item == 'Adanedhel':
            print(
                "Túrin the son of Húrin, though a Man, was raised from childhood in the halls of King Thingol of Doriath. When, later in his life, he went to dwell among the Elves of Nargothrond, "
                "they recognised the nobility he had learned in Thingol's kingdom, and gave him the name Adanedhel, meaning 'Elf-Man'.")
        elif item == 'Adûnakhôr':
            print("Cherries are often associated with love and romance, and are a popular gift on Valentine's Day.")
        elif item == 'Adûnaic':
            print(
                "Dates have been a staple food in the Middle East for thousands of years, and are rich in nutrients like fiber and potassium.")
        elif item == 'Adurant':
            print("")

    while True:
        again = input("Do you want to learn about something else? (yes or no): ")
        if again.lower() in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if again.lower() == 'no':
        break