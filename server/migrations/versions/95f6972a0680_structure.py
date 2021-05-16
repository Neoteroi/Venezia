"""structure

Revision ID: 95f6972a0680
Revises:
Create Date: 2021-05-16 20:24:03.448078

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "95f6972a0680"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "country",
        sa.Column("id", sa.String(2), primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
    )
    op.create_unique_constraint("uq_country_name", "country", ["name"])

    op.execute("CREATE UNIQUE INDEX country_name_uq_idx ON country (lower(name))")

    op.execute(
        """
        INSERT INTO Country (id, name) VALUES ('AF', N'Afghanistan');
        INSERT INTO Country (id, name) VALUES ('AL', N'Albania');
        INSERT INTO Country (id, name) VALUES ('DZ', N'Algeria');
        INSERT INTO Country (id, name) VALUES ('AS', N'American Samoa');
        INSERT INTO Country (id, name) VALUES ('AD', N'Andorra');
        INSERT INTO Country (id, name) VALUES ('AO', N'Angola');
        INSERT INTO Country (id, name) VALUES ('AI', N'Anguilla');
        INSERT INTO Country (id, name) VALUES ('AQ', N'Antarctica');
        INSERT INTO Country (id, name) VALUES ('AG', N'Antigua and Barbuda');
        INSERT INTO Country (id, name) VALUES ('AR', N'Argentina');
        INSERT INTO Country (id, name) VALUES ('AM', N'Armenia');
        INSERT INTO Country (id, name) VALUES ('AW', N'Aruba');
        INSERT INTO Country (id, name) VALUES ('AU', N'Australia');
        INSERT INTO Country (id, name) VALUES ('AT', N'Austria');
        INSERT INTO Country (id, name) VALUES ('AZ', N'Azerbaijan');
        INSERT INTO Country (id, name) VALUES ('BS', N'Bahamas');
        INSERT INTO Country (id, name) VALUES ('BH', N'Bahrain');
        INSERT INTO Country (id, name) VALUES ('BD', N'Bangladesh');
        INSERT INTO Country (id, name) VALUES ('BB', N'Barbados');
        INSERT INTO Country (id, name) VALUES ('BY', N'Belarus');
        INSERT INTO Country (id, name) VALUES ('BE', N'Belgium');
        INSERT INTO Country (id, name) VALUES ('BZ', N'Belize');
        INSERT INTO Country (id, name) VALUES ('BJ', N'Benin');
        INSERT INTO Country (id, name) VALUES ('BM', N'Bermuda');
        INSERT INTO Country (id, name) VALUES ('BT', N'Bhutan');
        INSERT INTO Country (id, name) VALUES ('BO', N'Bolivia');
        INSERT INTO Country (id, name) VALUES ('BA', N'Bosnia and Herzegovina');
        INSERT INTO Country (id, name) VALUES ('BW', N'Botswana');
        INSERT INTO Country (id, name) VALUES ('BV', N'Bouvet Island');
        INSERT INTO Country (id, name) VALUES ('BR', N'Brazil');
        INSERT INTO Country (id, name) VALUES ('IO', N'British Indian Ocean Territory');
        INSERT INTO Country (id, name) VALUES ('BN', N'Brunei');
        INSERT INTO Country (id, name) VALUES ('BG', N'Bulgaria');
        INSERT INTO Country (id, name) VALUES ('BF', N'Burkina Faso');
        INSERT INTO Country (id, name) VALUES ('BI', N'Burundi');
        INSERT INTO Country (id, name) VALUES ('KH', N'Cambodia');
        INSERT INTO Country (id, name) VALUES ('CM', N'Cameroon');
        INSERT INTO Country (id, name) VALUES ('CA', N'Canada');
        INSERT INTO Country (id, name) VALUES ('CV', N'Cape Verde');
        INSERT INTO Country (id, name) VALUES ('KY', N'Cayman Islands');
        INSERT INTO Country (id, name) VALUES ('CF', N'Central African Republic');
        INSERT INTO Country (id, name) VALUES ('TD', N'Chad');
        INSERT INTO Country (id, name) VALUES ('CL', N'Chile');
        INSERT INTO Country (id, name) VALUES ('CN', N'China');
        INSERT INTO Country (id, name) VALUES ('CX', N'Christmas Island');
        INSERT INTO Country (id, name) VALUES ('CC', N'Cocos (Keeling) Islands');
        INSERT INTO Country (id, name) VALUES ('CO', N'Colombia');
        INSERT INTO Country (id, name) VALUES ('KM', N'Comoros');
        INSERT INTO Country (id, name) VALUES ('CG', N'Congo');
        INSERT INTO Country (id, name) VALUES ('CD', N'Congo, the Democratic Republic of the');
        INSERT INTO Country (id, name) VALUES ('CK', N'Cook Islands');
        INSERT INTO Country (id, name) VALUES ('CR', N'Costa Rica');
        INSERT INTO Country (id, name) VALUES ('CI', N'Ivory Coast');
        INSERT INTO Country (id, name) VALUES ('HR', N'Croatia');
        INSERT INTO Country (id, name) VALUES ('CU', N'Cuba');
        INSERT INTO Country (id, name) VALUES ('CY', N'Cyprus');
        INSERT INTO Country (id, name) VALUES ('CZ', N'Czech Republic');
        INSERT INTO Country (id, name) VALUES ('DK', N'Denmark');
        INSERT INTO Country (id, name) VALUES ('DJ', N'Djibouti');
        INSERT INTO Country (id, name) VALUES ('DM', N'Dominica');
        INSERT INTO Country (id, name) VALUES ('DO', N'Dominican Republic');
        INSERT INTO Country (id, name) VALUES ('EC', N'Ecuador');
        INSERT INTO Country (id, name) VALUES ('EG', N'Egypt');
        INSERT INTO Country (id, name) VALUES ('SV', N'El Salvador');
        INSERT INTO Country (id, name) VALUES ('GQ', N'Equatorial Guinea');
        INSERT INTO Country (id, name) VALUES ('ER', N'Eritrea');
        INSERT INTO Country (id, name) VALUES ('EE', N'Estonia');
        INSERT INTO Country (id, name) VALUES ('ET', N'Ethiopia');
        INSERT INTO Country (id, name) VALUES ('FK', N'Falkland Islands (Malvinas)');
        INSERT INTO Country (id, name) VALUES ('FO', N'Faroe Islands');
        INSERT INTO Country (id, name) VALUES ('FJ', N'Fiji');
        INSERT INTO Country (id, name) VALUES ('FI', N'Finland');
        INSERT INTO Country (id, name) VALUES ('FR', N'France');
        INSERT INTO Country (id, name) VALUES ('GF', N'French Guiana');
        INSERT INTO Country (id, name) VALUES ('PF', N'French Polynesia');
        INSERT INTO Country (id, name) VALUES ('TF', N'French Southern Territories');
        INSERT INTO Country (id, name) VALUES ('GA', N'Gabon');
        INSERT INTO Country (id, name) VALUES ('GM', N'Gambia');
        INSERT INTO Country (id, name) VALUES ('GE', N'Georgia');
        INSERT INTO Country (id, name) VALUES ('DE', N'Germany');
        INSERT INTO Country (id, name) VALUES ('GH', N'Ghana');
        INSERT INTO Country (id, name) VALUES ('GI', N'Gibraltar');
        INSERT INTO Country (id, name) VALUES ('GR', N'Greece');
        INSERT INTO Country (id, name) VALUES ('GL', N'Greenland');
        INSERT INTO Country (id, name) VALUES ('GD', N'Grenada');
        INSERT INTO Country (id, name) VALUES ('GP', N'Guadeloupe');
        INSERT INTO Country (id, name) VALUES ('GU', N'Guam');
        INSERT INTO Country (id, name) VALUES ('GT', N'Guatemala');
        INSERT INTO Country (id, name) VALUES ('GG', N'Guernsey');
        INSERT INTO Country (id, name) VALUES ('GN', N'Guinea');
        INSERT INTO Country (id, name) VALUES ('GW', N'Guinea-Bissau');
        INSERT INTO Country (id, name) VALUES ('GY', N'Guyana');
        INSERT INTO Country (id, name) VALUES ('HT', N'Haiti');
        INSERT INTO Country (id, name) VALUES ('HM', N'Heard Island and McDonald Islands');
        INSERT INTO Country (id, name) VALUES ('VA', N'Holy See (Vatican City State)');
        INSERT INTO Country (id, name) VALUES ('HN', N'Honduras');
        INSERT INTO Country (id, name) VALUES ('HK', N'Hong Kong');
        INSERT INTO Country (id, name) VALUES ('HU', N'Hungary');
        INSERT INTO Country (id, name) VALUES ('IS', N'Iceland');
        INSERT INTO Country (id, name) VALUES ('IN', N'India');
        INSERT INTO Country (id, name) VALUES ('ID', N'Indonesia');
        INSERT INTO Country (id, name) VALUES ('IR', N'Iran');
        INSERT INTO Country (id, name) VALUES ('IQ', N'Iraq');
        INSERT INTO Country (id, name) VALUES ('IE', N'Ireland');
        INSERT INTO Country (id, name) VALUES ('IM', N'Isle of Man');
        INSERT INTO Country (id, name) VALUES ('IL', N'Israel');
        INSERT INTO Country (id, name) VALUES ('IT', N'Italy');
        INSERT INTO Country (id, name) VALUES ('JM', N'Jamaica');
        INSERT INTO Country (id, name) VALUES ('JP', N'Japan');
        INSERT INTO Country (id, name) VALUES ('JE', N'Jersey');
        INSERT INTO Country (id, name) VALUES ('JO', N'Jordan');
        INSERT INTO Country (id, name) VALUES ('KZ', N'Kazakhstan');
        INSERT INTO Country (id, name) VALUES ('KE', N'Kenya');
        INSERT INTO Country (id, name) VALUES ('KI', N'Kiribati');
        INSERT INTO Country (id, name) VALUES ('KP', N'Korea, Democratic People''s Republic of');
        INSERT INTO Country (id, name) VALUES ('KR', N'South Korea');
        INSERT INTO Country (id, name) VALUES ('KW', N'Kuwait');
        INSERT INTO Country (id, name) VALUES ('KG', N'Kyrgyzstan');
        INSERT INTO Country (id, name) VALUES ('LA', N'Lao People''s Democratic Republic');
        INSERT INTO Country (id, name) VALUES ('LV', N'Latvia');
        INSERT INTO Country (id, name) VALUES ('LB', N'Lebanon');
        INSERT INTO Country (id, name) VALUES ('LS', N'Lesotho');
        INSERT INTO Country (id, name) VALUES ('LR', N'Liberia');
        INSERT INTO Country (id, name) VALUES ('LY', N'Libya');
        INSERT INTO Country (id, name) VALUES ('LI', N'Liechtenstein');
        INSERT INTO Country (id, name) VALUES ('LT', N'Lithuania');
        INSERT INTO Country (id, name) VALUES ('LU', N'Luxembourg');
        INSERT INTO Country (id, name) VALUES ('MO', N'Macao');
        INSERT INTO Country (id, name) VALUES ('MK', N'North Macedonia');
        INSERT INTO Country (id, name) VALUES ('MG', N'Madagascar');
        INSERT INTO Country (id, name) VALUES ('MW', N'Malawi');
        INSERT INTO Country (id, name) VALUES ('MY', N'Malaysia');
        INSERT INTO Country (id, name) VALUES ('MV', N'Maldives');
        INSERT INTO Country (id, name) VALUES ('ML', N'Mali');
        INSERT INTO Country (id, name) VALUES ('MT', N'Malta');
        INSERT INTO Country (id, name) VALUES ('MH', N'Marshall Islands');
        INSERT INTO Country (id, name) VALUES ('MQ', N'Martinique');
        INSERT INTO Country (id, name) VALUES ('MR', N'Mauritania');
        INSERT INTO Country (id, name) VALUES ('MU', N'Mauritius');
        INSERT INTO Country (id, name) VALUES ('YT', N'Mayotte');
        INSERT INTO Country (id, name) VALUES ('MX', N'Mexico');
        INSERT INTO Country (id, name) VALUES ('FM', N'Micronesia, Federated States of');
        INSERT INTO Country (id, name) VALUES ('MD', N'Moldova');
        INSERT INTO Country (id, name) VALUES ('MC', N'Monaco');
        INSERT INTO Country (id, name) VALUES ('MN', N'Mongolia');
        INSERT INTO Country (id, name) VALUES ('ME', N'Montenegro');
        INSERT INTO Country (id, name) VALUES ('MS', N'Montserrat');
        INSERT INTO Country (id, name) VALUES ('MA', N'Morocco');
        INSERT INTO Country (id, name) VALUES ('MZ', N'Mozambique');
        INSERT INTO Country (id, name) VALUES ('MM', N'Myanmar');
        INSERT INTO Country (id, name) VALUES ('NA', N'Namibia');
        INSERT INTO Country (id, name) VALUES ('NR', N'Nauru');
        INSERT INTO Country (id, name) VALUES ('NP', N'Nepal');
        INSERT INTO Country (id, name) VALUES ('NL', N'Netherlands');
        INSERT INTO Country (id, name) VALUES ('AN', N'Netherlands Antilles');
        INSERT INTO Country (id, name) VALUES ('NC', N'New Caledonia');
        INSERT INTO Country (id, name) VALUES ('NZ', N'New Zealand');
        INSERT INTO Country (id, name) VALUES ('NI', N'Nicaragua');
        INSERT INTO Country (id, name) VALUES ('NE', N'Niger');
        INSERT INTO Country (id, name) VALUES ('NG', N'Nigeria');
        INSERT INTO Country (id, name) VALUES ('NU', N'Niue');
        INSERT INTO Country (id, name) VALUES ('NF', N'Norfolk Island');
        INSERT INTO Country (id, name) VALUES ('MP', N'Northern Mariana Islands');
        INSERT INTO Country (id, name) VALUES ('NO', N'Norway');
        INSERT INTO Country (id, name) VALUES ('OM', N'Oman');
        INSERT INTO Country (id, name) VALUES ('PK', N'Pakistan');
        INSERT INTO Country (id, name) VALUES ('PW', N'Palau');
        INSERT INTO Country (id, name) VALUES ('PS', N'Palestinian Territory, Occupied');
        INSERT INTO Country (id, name) VALUES ('PA', N'Panama');
        INSERT INTO Country (id, name) VALUES ('PG', N'Papua New Guinea');
        INSERT INTO Country (id, name) VALUES ('PY', N'Paraguay');
        INSERT INTO Country (id, name) VALUES ('PE', N'Peru');
        INSERT INTO Country (id, name) VALUES ('PH', N'Philippines');
        INSERT INTO Country (id, name) VALUES ('PN', N'Pitcairn');
        INSERT INTO Country (id, name) VALUES ('PL', N'Poland');
        INSERT INTO Country (id, name) VALUES ('PT', N'Portugal');
        INSERT INTO Country (id, name) VALUES ('PR', N'Puerto Rico');
        INSERT INTO Country (id, name) VALUES ('QA', N'Qatar');
        INSERT INTO Country (id, name) VALUES ('RE', N'Réunion');
        INSERT INTO Country (id, name) VALUES ('RO', N'Romania');
        INSERT INTO Country (id, name) VALUES ('RU', N'Russia');
        INSERT INTO Country (id, name) VALUES ('RW', N'Rwanda');
        INSERT INTO Country (id, name) VALUES ('SH', N'Saint Helena, Ascension and Tristan da Cunha');
        INSERT INTO Country (id, name) VALUES ('KN', N'Saint Kitts and Nevis');
        INSERT INTO Country (id, name) VALUES ('LC', N'Saint Lucia');
        INSERT INTO Country (id, name) VALUES ('PM', N'Saint Pierre and Miquelon');
        INSERT INTO Country (id, name) VALUES ('VC', N'Saint Vincent and the Grenadines');
        INSERT INTO Country (id, name) VALUES ('WS', N'Samoa');
        INSERT INTO Country (id, name) VALUES ('SM', N'San Marino');
        INSERT INTO Country (id, name) VALUES ('ST', N'Sao Tome and Principe');
        INSERT INTO Country (id, name) VALUES ('SA', N'Saudi Arabia');
        INSERT INTO Country (id, name) VALUES ('SN', N'Senegal');
        INSERT INTO Country (id, name) VALUES ('RS', N'Serbia');
        INSERT INTO Country (id, name) VALUES ('SC', N'Seychelles');
        INSERT INTO Country (id, name) VALUES ('SL', N'Sierra Leone');
        INSERT INTO Country (id, name) VALUES ('SG', N'Singapore');
        INSERT INTO Country (id, name) VALUES ('SK', N'Slovakia');
        INSERT INTO Country (id, name) VALUES ('SI', N'Slovenia');
        INSERT INTO Country (id, name) VALUES ('SB', N'Solomon Islands');
        INSERT INTO Country (id, name) VALUES ('SO', N'Somalia');
        INSERT INTO Country (id, name) VALUES ('ZA', N'South Africa');
        INSERT INTO Country (id, name) VALUES ('GS', N'South Georgia and the South Sandwich Islands');
        INSERT INTO Country (id, name) VALUES ('SS', N'South Sudan');
        INSERT INTO Country (id, name) VALUES ('ES', N'Spain');
        INSERT INTO Country (id, name) VALUES ('LK', N'Sri Lanka');
        INSERT INTO Country (id, name) VALUES ('SD', N'Sudan');
        INSERT INTO Country (id, name) VALUES ('SR', N'Suriname');
        INSERT INTO Country (id, name) VALUES ('SJ', N'Svalbard and Jan Mayen');
        INSERT INTO Country (id, name) VALUES ('SZ', N'Swaziland');
        INSERT INTO Country (id, name) VALUES ('SE', N'Sweden');
        INSERT INTO Country (id, name) VALUES ('CH', N'Switzerland');
        INSERT INTO Country (id, name) VALUES ('SY', N'Syrian Arab Republic');
        INSERT INTO Country (id, name) VALUES ('TW', N'Taiwan');
        INSERT INTO Country (id, name) VALUES ('TJ', N'Tajikistan');
        INSERT INTO Country (id, name) VALUES ('TZ', N'Tanzania, United Republic of');
        INSERT INTO Country (id, name) VALUES ('TH', N'Thailand');
        INSERT INTO Country (id, name) VALUES ('TL', N'Timor-Leste');
        INSERT INTO Country (id, name) VALUES ('TG', N'Togo');
        INSERT INTO Country (id, name) VALUES ('TK', N'Tokelau');
        INSERT INTO Country (id, name) VALUES ('TO', N'Tonga');
        INSERT INTO Country (id, name) VALUES ('TT', N'Trinidad and Tobago');
        INSERT INTO Country (id, name) VALUES ('TN', N'Tunisia');
        INSERT INTO Country (id, name) VALUES ('TR', N'Turkey');
        INSERT INTO Country (id, name) VALUES ('TM', N'Turkmenistan');
        INSERT INTO Country (id, name) VALUES ('TC', N'Turks and Caicos Islands');
        INSERT INTO Country (id, name) VALUES ('TV', N'Tuvalu');
        INSERT INTO Country (id, name) VALUES ('UG', N'Uganda');
        INSERT INTO Country (id, name) VALUES ('UA', N'Ukraine');
        INSERT INTO Country (id, name) VALUES ('AE', N'United Arab Emirates');
        INSERT INTO Country (id, name) VALUES ('GB', N'United Kingdom');
        INSERT INTO Country (id, name) VALUES ('US', N'United States');
        INSERT INTO Country (id, name) VALUES ('UM', N'United States Minor Outlying Islands');
        INSERT INTO Country (id, name) VALUES ('UY', N'Uruguay');
        INSERT INTO Country (id, name) VALUES ('UZ', N'Uzbekistan');
        INSERT INTO Country (id, name) VALUES ('VU', N'Vanuatu');
        INSERT INTO Country (id, name) VALUES ('VE', N'Venezuela');
        INSERT INTO Country (id, name) VALUES ('VN', N'Vietnam');
        INSERT INTO Country (id, name) VALUES ('VG', N'Virgin Islands, British');
        INSERT INTO Country (id, name) VALUES ('VI', N'Virgin Islands, U.S.');
        INSERT INTO Country (id, name) VALUES ('WF', N'Wallis and Futuna');
        INSERT INTO Country (id, name) VALUES ('EH', N'Western Sahara');
        INSERT INTO Country (id, name) VALUES ('YE', N'Yemen');
        INSERT INTO Country (id, name) VALUES ('ZM', N'Zambia');
        INSERT INTO Country (id, name) VALUES ('ZW', N'Zimbabwe');
    """
    )


def downgrade():
    op.drop_table("country")
