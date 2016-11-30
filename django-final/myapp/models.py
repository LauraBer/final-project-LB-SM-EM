from django.db import models

# Create your models here.

LGAs = (
    ('Balonne', 'Balonne'),
    ('Banana', 'Banana'),
    ('Barcaldine', 'Barcaldine'),
    ('Barcoo', 'Barcoo'),
    ('Blackall Tambo', 'Blackall Tambo'),
    ('Boulia', 'Boulia'),
    ('Brisbane', 'Brisbane'),
    ('Bundaberg', 'Bundaberg'),
    ('Burdekin', 'Burdekin'),
    ('Burke', 'Burke'),
    ('Cairns', 'Cairns'),
    ('Carpentaria', 'Carpentaria'),
    ('Cassowary Coast', 'Cassowary Coast'),
    ('Central Highlands', 'Central Highlands'),
    ('Charters Towers', 'Charters Towers'),
    ('Cloncurry', 'Cloncurry'),
    ('Cook', 'Cook'),
    ('Croydon', 'Croydon'),
    ('Diamantina', 'Diamantina'),
    ('Douglas', 'Douglas'),
    ('Etheridge', 'Etheridge'),
    ('Flinders', 'Flinders'),
    ('Fraser Coast', 'Fraser Coast'),
    ('Gladstone', 'Gladstone'),
    ('Gold Coast', 'Gold Coast'),
    ('Goondiwindi', 'Goondiwindi'),
    ('Gympie', 'Gympie'),
    ('Hinchinbrook', 'Hinchinbrook'),
    ('Ipswich', 'Ipswich'),
    ('Isaac', 'Isaac'),
    ('Livingstone', 'Livingstone'),
    ('Lockyer Valley', 'Lockyer Valley'),
    ('Logan', 'Logan'),
    ('Longreach', 'Longreach'),
    ('Mackay', 'Mackay'),
    ('Mareeba', 'Mareeba'),
    ('Mckinlay', 'Mckinlay'),
    ('Moreton Bay', 'Moreton Bay'),
    ('Mount Isa', 'Mount Isa'),
    ('Murweh', 'Murweh'),
    ('Noosa', 'Noosa'),
    ('North Burnett', 'North Burnett'),
    ('Paroo', 'Paroo'),
    ('Quilpie', 'Quilpie'),
    ('Redland', 'Redland'),
    ('Richmond', 'Richmond'),
    ('Rockhampton', 'Rockhampton'),
    ('Scenic Rim', 'Scenic Rim'),
    ('Somerset', 'Somerset'),
    ('South Burnett', 'South Burnett'),
    ('Southern Downs', 'Southern Downs'),
    ('Sunshine Coast', 'Sunshine Coast'),
    ('Tablelands', 'Tablelands'),
    ('Toowoomba', 'Toowoomba'),
    ('Torres', 'Torres'),
    ('Townsville', 'Townsville'),
    ('Western Downs', 'Western Downs'),
    ('Whitsunday', 'Whitsunday'),
    ('Winton', 'Winton'),
   )

LGAs_DICT = dict(LGAs)

class Input(models.Model):

    lga = models.CharField(max_length=2, choices=LGAs)
    name  = models.CharField(max_length=50)
