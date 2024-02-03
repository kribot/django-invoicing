# Generated by Django 5.0 on 2024-01-22 16:12

import django.core.validators
import django_countries.fields
import internationalflavor.vat_number.models
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0030_invoice_supplier_is_vat_payer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='already_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='already paid'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='attachments',
            field=models.JSONField(blank=True, default=None, null=True, verbose_name='attachments'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bank_city',
            field=models.CharField(blank=True, max_length=255, verbose_name='bank city'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bank_country',
            field=django_countries.fields.CountryField(blank=True, max_length=255, verbose_name='bank country'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bank_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='bank name'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bank_street',
            field=models.CharField(blank=True, max_length=255, verbose_name='bank street and number'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bank_zip',
            field=models.CharField(blank=True, max_length=255, verbose_name='bank ZIP'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='constant_symbol',
            field=models.CharField(blank=True, choices=[('0001', '0001 - Payments for goods based on legal and executable decision from legal authority'), ('0008', '0008 - Cashless payments for goods'), ('0038', '0038 - Cashless funds for wages'), ('0058', '0058 - Cashless penalty and delinquency charges'), ('0068', '0068 - Transfer of funds for wages and other personal costs'), ('0138', '0138 - Cashless deductions at source'), ('0168', '0168 - Cashless payments in loans'), ('0178', '0178 - Sales from provided services'), ('0298', '0298 - Other cashless transfers'), ('0304', '0304 - Prior payments for services'), ('0308', '0308 - Cashless payments for services'), ('0358', '0358 - Payments dedicated to payout through post offices'), ('0379', '0379 - Other income, income from postal order'), ('0498', '0498 - Payments in loans'), ('0558', '0558 - Cashless other financial payments'), ('0934', '0934 - Benefits - prior payments'), ('0968', '0968 - Other cashless transfers'), ('1144', '1144 - Prior payment - advance'), ('1148', '1148 - Payment - current advance'), ('1744', '1744 - Accounting of tax at income tax of physical body and corporate body'), ('1748', '1748 - Income tax of physical body and corporate body based on declared tax year'), ('3118', '3118 - Insurance and empl. contrib. to insur. co. and the Labor Office'), ('3344', '3344 - Penalty from message - prior'), ('3348', '3348 - Penalty from message'), ('3354', '3354 - Insurance payments by insurance companies'), ('3558', '3558 - Cashless insurance payments by insurance companies'), ('8147', '8147 - Payment (posted together with the instruction)')], max_length=64, verbose_name='constant symbol'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='currency',
            field=models.CharField(choices=[('XUA', 'ADB Unit of Account'), ('AFN', 'Afghan Afghani'), ('AFA', 'Afghan Afghani (1927–2002)'), ('ALL', 'Albanian Lek'), ('ALK', 'Albanian Lek (1946–1965)'), ('DZD', 'Algerian Dinar'), ('ADP', 'Andorran Peseta'), ('AOA', 'Angolan Kwanza'), ('AOK', 'Angolan Kwanza (1977–1991)'), ('AON', 'Angolan New Kwanza (1990–2000)'), ('AOR', 'Angolan Readjusted Kwanza (1995–1999)'), ('ARA', 'Argentine Austral'), ('ARS', 'Argentine Peso'), ('ARM', 'Argentine Peso (1881–1970)'), ('ARP', 'Argentine Peso (1983–1985)'), ('ARL', 'Argentine Peso Ley (1970–1983)'), ('AMD', 'Armenian Dram'), ('AWG', 'Aruban Florin'), ('AUD', 'Australian Dollar'), ('ATS', 'Austrian Schilling'), ('AZN', 'Azerbaijani Manat'), ('AZM', 'Azerbaijani Manat (1993–2006)'), ('BSD', 'Bahamian Dollar'), ('BHD', 'Bahraini Dinar'), ('BDT', 'Bangladeshi Taka'), ('BBD', 'Barbadian Dollar'), ('BYN', 'Belarusian Ruble'), ('BYB', 'Belarusian Ruble (1994–1999)'), ('BYR', 'Belarusian Ruble (2000–2016)'), ('BEF', 'Belgian Franc'), ('BEC', 'Belgian Franc (convertible)'), ('BEL', 'Belgian Franc (financial)'), ('BZD', 'Belize Dollar'), ('BMD', 'Bermudan Dollar'), ('BTN', 'Bhutanese Ngultrum'), ('BOB', 'Bolivian Boliviano'), ('BOL', 'Bolivian Boliviano (1863–1963)'), ('BOV', 'Bolivian Mvdol'), ('BOP', 'Bolivian Peso'), ('VED', 'Bolívar Soberano'), ('BAM', 'Bosnia-Herzegovina Convertible Mark'), ('BAD', 'Bosnia-Herzegovina Dinar (1992–1994)'), ('BAN', 'Bosnia-Herzegovina New Dinar (1994–1997)'), ('BWP', 'Botswanan Pula'), ('BRC', 'Brazilian Cruzado (1986–1989)'), ('BRZ', 'Brazilian Cruzeiro (1942–1967)'), ('BRE', 'Brazilian Cruzeiro (1990–1993)'), ('BRR', 'Brazilian Cruzeiro (1993–1994)'), ('BRN', 'Brazilian New Cruzado (1989–1990)'), ('BRB', 'Brazilian New Cruzeiro (1967–1986)'), ('BRL', 'Brazilian Real'), ('GBP', 'British Pound'), ('BND', 'Brunei Dollar'), ('BGL', 'Bulgarian Hard Lev'), ('BGN', 'Bulgarian Lev'), ('BGO', 'Bulgarian Lev (1879–1952)'), ('BGM', 'Bulgarian Socialist Lev'), ('BUK', 'Burmese Kyat'), ('BIF', 'Burundian Franc'), ('XPF', 'CFP Franc'), ('KHR', 'Cambodian Riel'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verdean Escudo'), ('KYD', 'Cayman Islands Dollar'), ('XAF', 'Central African CFA Franc'), ('CLE', 'Chilean Escudo'), ('CLP', 'Chilean Peso'), ('CLF', 'Chilean Unit of Account (UF)'), ('CNX', 'Chinese People’s Bank Dollar'), ('CNY', 'Chinese Yuan'), ('CNH', 'Chinese Yuan (offshore)'), ('COP', 'Colombian Peso'), ('COU', 'Colombian Real Value Unit'), ('KMF', 'Comorian Franc'), ('CDF', 'Congolese Franc'), ('CRC', 'Costa Rican Colón'), ('HRD', 'Croatian Dinar'), ('HRK', 'Croatian Kuna'), ('CUC', 'Cuban Convertible Peso'), ('CUP', 'Cuban Peso'), ('CYP', 'Cypriot Pound'), ('CZK', 'Czech Koruna'), ('CSK', 'Czechoslovak Hard Koruna'), ('DKK', 'Danish Krone'), ('DJF', 'Djiboutian Franc'), ('DOP', 'Dominican Peso'), ('NLG', 'Dutch Guilder'), ('XCD', 'East Caribbean Dollar'), ('DDM', 'East German Mark'), ('ECS', 'Ecuadorian Sucre'), ('ECV', 'Ecuadorian Unit of Constant Value'), ('EGP', 'Egyptian Pound'), ('GQE', 'Equatorial Guinean Ekwele'), ('ERN', 'Eritrean Nakfa'), ('EEK', 'Estonian Kroon'), ('ETB', 'Ethiopian Birr'), ('EUR', 'Euro'), ('XBA', 'European Composite Unit'), ('XEU', 'European Currency Unit'), ('XBB', 'European Monetary Unit'), ('XBC', 'European Unit of Account (XBC)'), ('XBD', 'European Unit of Account (XBD)'), ('FKP', 'Falkland Islands Pound'), ('FJD', 'Fijian Dollar'), ('FIM', 'Finnish Markka'), ('FRF', 'French Franc'), ('XFO', 'French Gold Franc'), ('XFU', 'French UIC-Franc'), ('GMD', 'Gambian Dalasi'), ('GEK', 'Georgian Kupon Larit'), ('GEL', 'Georgian Lari'), ('DEM', 'German Mark'), ('GHS', 'Ghanaian Cedi'), ('GHC', 'Ghanaian Cedi (1979–2007)'), ('GIP', 'Gibraltar Pound'), ('XAU', 'Gold'), ('GRD', 'Greek Drachma'), ('GTQ', 'Guatemalan Quetzal'), ('GWP', 'Guinea-Bissau Peso'), ('GNF', 'Guinean Franc'), ('GNS', 'Guinean Syli'), ('GYD', 'Guyanaese Dollar'), ('HTG', 'Haitian Gourde'), ('HNL', 'Honduran Lempira'), ('HKD', 'Hong Kong Dollar'), ('HUF', 'Hungarian Forint'), ('IMP', 'IMP'), ('ISK', 'Icelandic Króna'), ('ISJ', 'Icelandic Króna (1918–1981)'), ('INR', 'Indian Rupee'), ('IDR', 'Indonesian Rupiah'), ('IRR', 'Iranian Rial'), ('IQD', 'Iraqi Dinar'), ('IEP', 'Irish Pound'), ('ILS', 'Israeli New Shekel'), ('ILP', 'Israeli Pound'), ('ILR', 'Israeli Shekel (1980–1985)'), ('ITL', 'Italian Lira'), ('JMD', 'Jamaican Dollar'), ('JPY', 'Japanese Yen'), ('JOD', 'Jordanian Dinar'), ('KZT', 'Kazakhstani Tenge'), ('KES', 'Kenyan Shilling'), ('KWD', 'Kuwaiti Dinar'), ('KGS', 'Kyrgystani Som'), ('LAK', 'Laotian Kip'), ('LVL', 'Latvian Lats'), ('LVR', 'Latvian Ruble'), ('LBP', 'Lebanese Pound'), ('LSL', 'Lesotho Loti'), ('LRD', 'Liberian Dollar'), ('LYD', 'Libyan Dinar'), ('LTL', 'Lithuanian Litas'), ('LTT', 'Lithuanian Talonas'), ('LUL', 'Luxembourg Financial Franc'), ('LUC', 'Luxembourgian Convertible Franc'), ('LUF', 'Luxembourgian Franc'), ('MOP', 'Macanese Pataca'), ('MKD', 'Macedonian Denar'), ('MKN', 'Macedonian Denar (1992–1993)'), ('MGA', 'Malagasy Ariary'), ('MGF', 'Malagasy Franc'), ('MWK', 'Malawian Kwacha'), ('MYR', 'Malaysian Ringgit'), ('MVR', 'Maldivian Rufiyaa'), ('MVP', 'Maldivian Rupee (1947–1981)'), ('MLF', 'Malian Franc'), ('MTL', 'Maltese Lira'), ('MTP', 'Maltese Pound'), ('MRU', 'Mauritanian Ouguiya'), ('MRO', 'Mauritanian Ouguiya (1973–2017)'), ('MUR', 'Mauritian Rupee'), ('MXV', 'Mexican Investment Unit'), ('MXN', 'Mexican Peso'), ('MXP', 'Mexican Silver Peso (1861–1992)'), ('MDC', 'Moldovan Cupon'), ('MDL', 'Moldovan Leu'), ('MCF', 'Monegasque Franc'), ('MNT', 'Mongolian Tugrik'), ('MAD', 'Moroccan Dirham'), ('MAF', 'Moroccan Franc'), ('MZE', 'Mozambican Escudo'), ('MZN', 'Mozambican Metical'), ('MZM', 'Mozambican Metical (1980–2006)'), ('MMK', 'Myanmar Kyat'), ('NAD', 'Namibian Dollar'), ('NPR', 'Nepalese Rupee'), ('ANG', 'Netherlands Antillean Guilder'), ('TWD', 'New Taiwan Dollar'), ('NZD', 'New Zealand Dollar'), ('NIO', 'Nicaraguan Córdoba'), ('NIC', 'Nicaraguan Córdoba (1988–1991)'), ('NGN', 'Nigerian Naira'), ('KPW', 'North Korean Won'), ('NOK', 'Norwegian Krone'), ('OMR', 'Omani Rial'), ('PKR', 'Pakistani Rupee'), ('XPD', 'Palladium'), ('PAB', 'Panamanian Balboa'), ('PGK', 'Papua New Guinean Kina'), ('PYG', 'Paraguayan Guarani'), ('PEI', 'Peruvian Inti'), ('PEN', 'Peruvian Sol'), ('PES', 'Peruvian Sol (1863–1965)'), ('PHP', 'Philippine Peso'), ('XPT', 'Platinum'), ('PLN', 'Polish Zloty'), ('PLZ', 'Polish Zloty (1950–1995)'), ('PTE', 'Portuguese Escudo'), ('GWE', 'Portuguese Guinea Escudo'), ('QAR', 'Qatari Riyal'), ('XRE', 'RINET Funds'), ('RHD', 'Rhodesian Dollar'), ('RON', 'Romanian Leu'), ('ROL', 'Romanian Leu (1952–2006)'), ('RUB', 'Russian Ruble'), ('RUR', 'Russian Ruble (1991–1998)'), ('RWF', 'Rwandan Franc'), ('SVC', 'Salvadoran Colón'), ('WST', 'Samoan Tala'), ('SAR', 'Saudi Riyal'), ('RSD', 'Serbian Dinar'), ('CSD', 'Serbian Dinar (2002–2006)'), ('SCR', 'Seychellois Rupee'), ('SLE', 'Sierra Leonean Leone'), ('SLL', 'Sierra Leonean Leone (1964—2022)'), ('XAG', 'Silver'), ('SGD', 'Singapore Dollar'), ('SKK', 'Slovak Koruna'), ('SIT', 'Slovenian Tolar'), ('SBD', 'Solomon Islands Dollar'), ('SOS', 'Somali Shilling'), ('ZAR', 'South African Rand'), ('ZAL', 'South African Rand (financial)'), ('KRH', 'South Korean Hwan (1953–1962)'), ('KRW', 'South Korean Won'), ('KRO', 'South Korean Won (1945–1953)'), ('SSP', 'South Sudanese Pound'), ('SUR', 'Soviet Rouble'), ('ESP', 'Spanish Peseta'), ('ESA', 'Spanish Peseta (A account)'), ('ESB', 'Spanish Peseta (convertible account)'), ('XDR', 'Special Drawing Rights'), ('LKR', 'Sri Lankan Rupee'), ('SHP', 'St. Helena Pound'), ('XSU', 'Sucre'), ('SDD', 'Sudanese Dinar (1992–2007)'), ('SDG', 'Sudanese Pound'), ('SDP', 'Sudanese Pound (1957–1998)'), ('SRD', 'Surinamese Dollar'), ('SRG', 'Surinamese Guilder'), ('SZL', 'Swazi Lilangeni'), ('SEK', 'Swedish Krona'), ('CHF', 'Swiss Franc'), ('SYP', 'Syrian Pound'), ('STN', 'São Tomé & Príncipe Dobra'), ('STD', 'São Tomé & Príncipe Dobra (1977–2017)'), ('TVD', 'TVD'), ('TJR', 'Tajikistani Ruble'), ('TJS', 'Tajikistani Somoni'), ('TZS', 'Tanzanian Shilling'), ('XTS', 'Testing Currency Code'), ('THB', 'Thai Baht'), ('TPE', 'Timorese Escudo'), ('TOP', 'Tongan Paʻanga'), ('TTD', 'Trinidad & Tobago Dollar'), ('TND', 'Tunisian Dinar'), ('TRY', 'Turkish Lira'), ('TRL', 'Turkish Lira (1922–2005)'), ('TMT', 'Turkmenistani Manat'), ('TMM', 'Turkmenistani Manat (1993–2009)'), ('USD', 'US Dollar'), ('USN', 'US Dollar (Next day)'), ('USS', 'US Dollar (Same day)'), ('UGX', 'Ugandan Shilling'), ('UGS', 'Ugandan Shilling (1966–1987)'), ('UAH', 'Ukrainian Hryvnia'), ('UAK', 'Ukrainian Karbovanets'), ('AED', 'United Arab Emirates Dirham'), ('UYW', 'Uruguayan Nominal Wage Index Unit'), ('UYU', 'Uruguayan Peso'), ('UYP', 'Uruguayan Peso (1975–1993)'), ('UYI', 'Uruguayan Peso (Indexed Units)'), ('UZS', 'Uzbekistani Som'), ('VUV', 'Vanuatu Vatu'), ('VES', 'Venezuelan Bolívar'), ('VEB', 'Venezuelan Bolívar (1871–2008)'), ('VEF', 'Venezuelan Bolívar (2008–2018)'), ('VND', 'Vietnamese Dong'), ('VNN', 'Vietnamese Dong (1978–1985)'), ('CHE', 'WIR Euro'), ('CHW', 'WIR Franc'), ('XOF', 'West African CFA Franc'), ('YDD', 'Yemeni Dinar'), ('YER', 'Yemeni Rial'), ('YUN', 'Yugoslavian Convertible Dinar (1990–1992)'), ('YUD', 'Yugoslavian Hard Dinar (1966–1990)'), ('YUM', 'Yugoslavian New Dinar (1994–2002)'), ('YUR', 'Yugoslavian Reformed Dinar (1992–1993)'), ('ZWN', 'ZWN'), ('ZRN', 'Zairean New Zaire (1993–1998)'), ('ZRZ', 'Zairean Zaire (1971–1993)'), ('ZMW', 'Zambian Kwacha'), ('ZMK', 'Zambian Kwacha (1968–2012)'), ('ZWD', 'Zimbabwean Dollar (1980–2008)'), ('ZWR', 'Zimbabwean Dollar (2008)'), ('ZWL', 'Zimbabwean Dollar (2009)')], max_length=10, verbose_name='currency'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_city',
            field=models.CharField(blank=True, max_length=255, verbose_name='customer city'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='customer email'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_phone',
            field=models.CharField(blank=True, max_length=255, verbose_name='customer phone'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_registration_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='customer Reg. No.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_street',
            field=models.CharField(blank=True, max_length=255, verbose_name='customer street and number'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_tax_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='customer Tax No.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_vat_id',
            field=internationalflavor.vat_number.models.VATNumberField(blank=True, verbose_name='customer VAT No.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_zip',
            field=models.CharField(blank=True, max_length=255, verbose_name='customer ZIP'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_paid',
            field=model_utils.fields.MonitorField(blank=True, default=None, monitor='status', null=True, verbose_name='date paid', when={'PAID'}),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_reminder_sent',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='date reminder sent'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_sent',
            field=model_utils.fields.MonitorField(blank=True, default=None, monitor='status', null=True, verbose_name='date sent', when={'SENT'}),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='delivery_method',
            field=models.CharField(choices=[('PERSONAL_PICKUP', 'personal pickup'), ('MAILING', 'mailing'), ('DIGITAL', 'digital')], default='PERSONAL_PICKUP', max_length=64, verbose_name='delivery method'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='issuer_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='issuer email'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='issuer_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='issuer name'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='issuer_phone',
            field=models.CharField(blank=True, max_length=255, verbose_name='issuer phone'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='language',
            field=models.CharField(choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ar-dz', 'Algerian Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('ckb', 'Central Kurdish (Sorani)'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dsb', 'Lower Sorbian'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hsb', 'Upper Sorbian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('ig', 'Igbo'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kab', 'Kabyle'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('ky', 'Kyrgyz'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('ms', 'Malay'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmål'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('tk', 'Turkmen'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('ug', 'Uyghur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')], max_length=10, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='note',
            field=models.CharField(blank=True, default='Thank you for using our services.', max_length=255, verbose_name='note'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.CharField(blank=True, max_length=128, verbose_name='number'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_method',
            field=models.CharField(choices=[('BANK_TRANSFER', 'bank transfer'), ('CASH', 'cash'), ('CASH_ON_DELIVERY', 'cash on delivery'), ('PAYMENT_CARD', 'payment card')], max_length=64, verbose_name='payment method'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='reference',
            field=models.CharField(blank=True, max_length=140, verbose_name='reference'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='related_document',
            field=models.CharField(blank=True, max_length=100, verbose_name='related document'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='related_invoices',
            field=models.ManyToManyField(blank=True, to='invoicing.invoice', verbose_name='related invoices'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='sequence',
            field=models.IntegerField(blank=True, db_index=True, verbose_name='sequence'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_city',
            field=models.CharField(blank=True, max_length=255, verbose_name='shipping city'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='shipping country'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='shipping name'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_street',
            field=models.CharField(blank=True, max_length=255, verbose_name='shipping street and number'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_zip',
            field=models.CharField(blank=True, max_length=255, verbose_name='shipping ZIP'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('NEW', 'new'), ('SENT', 'sent'), ('RETURNED', 'returned'), ('CANCELED', 'canceled'), ('PAID', 'paid'), ('CREDITED', 'credited'), ('UNCOLLECTIBLE', 'uncollectible')], default='NEW', max_length=64, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, verbose_name='subtitle'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_additional_info',
            field=models.JSONField(blank=True, default=None, null=True, verbose_name='supplier additional information'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_city',
            field=models.CharField(blank=True, max_length=255, verbose_name='supplier city'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_is_vat_payer',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='supplier is VAT payer'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_registration_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='supplier Reg. No.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_street',
            field=models.CharField(blank=True, max_length=255, verbose_name='supplier street and number'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_tax_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='supplier Tax No.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_vat_id',
            field=internationalflavor.vat_number.models.VATNumberField(blank=True, verbose_name='supplier VAT No.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_zip',
            field=models.CharField(blank=True, max_length=255, verbose_name='supplier ZIP'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='total'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='type',
            field=models.CharField(choices=[('INVOICE', 'Invoice'), ('ADVANCE', 'Advance invoice'), ('PROFORMA', 'Proforma invoice'), ('CREDIT_NOTE', 'Credit note')], default='INVOICE', max_length=64, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='vat',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='VAT'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.TextField(verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='item',
            name='unit',
            field=models.CharField(choices=[('EMPTY', ''), ('PIECES', 'pcs.'), ('HOURS', 'hours')], default='PIECES', max_length=64, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], default=0, help_text='ordering', null=True, verbose_name='weight'),
        ),
    ]
