# Generated by Django 2.2 on 2019-09-13 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20190913_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='region',
            field=models.CharField(choices=[('Alberni-Clayoquot', 'Alberni-Clayoquot'), ('Bulkley-Nechako', 'Buckley-Nechako'), ('Capital', 'Capital'), ('Cariboo', 'Cariboo'), ('Central Coast', 'Central Coast'), ('Central Kootenay', 'Central Kootenay'), ('Central Okanagan', 'Central Okanagan'), ('Columnbia Shuswap', 'Columbia Shuswap'), ('Comox Valley', 'Comox Valley'), ('Cowichan Valley', 'Cowichan Valley'), ('East Kootenay', 'East Kootenay'), ('Fraser Valley', 'Fraser Valley'), ('Fraser-Fort George', 'Fraser-Fort George'), ('Islands Trust', 'Islands Trust'), ('Kitimat Stikine', 'Kitimat-Stikine'), ('Kootenay Boundary', 'Kootenay-Boundary'), ('Metro Vancouver', 'Metro Vancouver'), ('Mount Waddington', 'Mount Waddington'), ('Nanaimo', 'Nanaimo'), ('North Okanagan', 'North Okanagan'), ('North Coast', 'North Coast'), ('Okanagan-Similkameen', 'Okanagan-Similkameen'), ('Peace River', 'Peace River'), ('Gathet', 'qathet'), ('Squamish-Lillooet', 'Squamish-Lillooet'), ('Strathcona', 'Strathcona'), ('Sunshine Coast', 'Sunshine Coast'), ('Thompson-Nicola', 'Thompson-Nicola')], default='', max_length=20),
        ),
    ]
