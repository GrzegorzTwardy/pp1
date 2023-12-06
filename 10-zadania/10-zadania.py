def z8():
    class Phone():
        def __init__(self, brand, model, price):
            self.brand = brand
            self.model = model
            self.price = price
            
        def show_price(self):
            print(f'The phone costs: {self.price} zł.')

        def from_usa(self):
            if self.brand == 'Apple':
                return 'USA'
            else:
                return 'not USA'

        def change_price(self, new_price):
            self.price = new_price


    phone_1 = Phone('Samsung', 'Galaxy', '2300')

    print(f'The phone\'s brand is {phone_1.brand}')
    print(f'The phone\'s model is {phone_1.model}')
    phone_1.show_price()

    print(f'The phone\'s country of origin is {phone_1.from_usa()}.')
    phone_1.change_price(3600)

    phone_1.show_price()


def z9():
    class University():

        def __init__(self, name):
            self.name = name 
        
        def __str__(self):
            return self.name + " is the best!"
        
    my_university = University('KUE')
    print(my_university)      


def z10():
    class Track():

        def __init__(self, artist, title, album, year):
            self.artist = artist
            self.title = title
            self.album = album
            self.year = year

        def __str__(self):
            return f"""
            Performer: {self.artist}
            Song: {self.title}
            Album: {self.album}
            Year: {self.year}
            """

    track_1 = Track('ar1', 'title1', 'album1', '2001')
    track_2 = Track('ar2', 'title2', 'album2', '2002')

    print(track_1, track_2)


def z11():
    class Tv():

        def __init__(self):
            self.is_on = False

        def turn_on(self):
            self.is_on = True

        def turn_off(self):
            self.is_on = False

        def show_status(self):
            if self.is_on:
                print('TV is on')
            else:
                print('TV is off')

        
    tv = Tv()
    tv.show_status()
    tv.turn_on()
    tv.show_status()
    tv.turn_off()
    tv.show_status()


def z12():
    class Tv():

        def __init__(self):
            self.is_on = False
            self.channel_no = 1

        def turn_on(self):
            self.is_on = True

        def turn_off(self):
            self.is_on = False

        def show_status(self):
            if self.is_on:
                print(f'TV is on, channel {self.channel_no}')
            else:
                print('TV is off')

    tv = Tv()
    tv.turn_on()
    tv.show_status()    


def z13():
    class Tv():

        def __init__(self):
            self.is_on = False
            self.channel_no = 1

        def turn_on(self):
            self.is_on = True

        def turn_off(self):
            self.is_on = False

        def show_status(self):
            if self.is_on:
                print(f'TV is on, channel {self.channel_no}')
            else:
                print('TV is off')

        def set_channel(self, new):
            self.channel_no = new


    tv = Tv()
    tv.show_status()
    tv.turn_on()
    tv.show_status()
    tv.set_channel(5)
    tv.show_status()
    tv.turn_off()
    tv.show_status()


def z14_15():
    class Tv():

        def __init__(self):
            self.is_on = False
            self.channel_no = 1
            self.channels = []

        def turn_on(self):
            self.is_on = True

        def turn_off(self):
            self.is_on = False

        def show_status(self):
            if self.is_on:
                if self.channels:
                    print(f'TV is on, channel {self.channel_no} ({self.channels[self.channel_no-1]})')
                else:
                    print(f'TV is on, no channels available')
            else:
                print('TV is off')

        def set_channel(self, new):
            self.channel_no = new

        def set_channels(self, channels_list):
            self.channels = channels_list

        def show_channels(self):
            if self.channels:
                print('Channel list:')

                for i in range(len(self.channels)):
                    print(f'{i+1}. {self.channels[i]}')
            else:
                print('There are no channels available.')


    channels = ['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery', 'BBC']

    tv = Tv()
    tv.show_status()
    tv.turn_on()
    tv.show_status()
    tv.show_channels()
    tv.set_channels(channels)
    tv.show_channels()
    tv.show_status()
    tv.turn_off()

    print('\nzadanie 15')
    tv.turn_on()
    tv.set_channel(7)
    tv.show_status()


def z16():
    class Phone():

        def __init__(self, brand, model, price):
            self.brand = brand
            self.model = model
            self.price = price
            self.fully_charged = True 


        def __str__(self):
            return f"""
            Brand: {self.brand}
            Model: {self.model}
            Price: {self.price}
            """

        def is_charged(self):
            if self.fully_charged:
                print('The phone is fully charged.')
            else:
                print('The phone isn\'t fully charged.')


        def change_price(self, new_price):
            self.price = new_price


    phone_1 = Phone('Samsung', 'Galaxy', 2400)
    phone_2 = Phone('Iphone', '6s', 7000000)

    print(phone_1, phone_2)

        
def z17():
    class Tv():

        def __init__(self):
            self.is_on = False
            self.channel_no = 1
            self.channels = []
            self.volume = 0

        def turn_on(self):
            self.is_on = True

        def turn_off(self):
            self.is_on = False

        def show_status(self):
            if self.is_on:
                if self.channels:
                    print(f'TV is on, channel {self.channel_no} ({self.channels[self.channel_no-1]})')
                else:
                    print(f'TV is on, no channels available')
            else:
                print('TV is off')

        def set_channel(self, new):
            self.channel_no = new

        def set_channels(self, channels_list):
            self.channels = channels_list

        def show_channels(self):
            if self.channels:
                print('Channel list:')

                for i in range(len(self.channels)):
                    print(f'{i+1}. {self.channels[i]}')
            else:
                print('There are no channels available.')

        # def increase_vol(self, new_vol):
            

    channels = ['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery', 'BBC']

    tv = Tv()
    tv.show_status()
    tv.turn_on()
    tv.show_status()
    tv.show_channels()
    tv.set_channels(channels)
    tv.show_channels()
    tv.show_status()
    tv.turn_off()

    print('\nzadanie 15')
    tv.turn_on()
    tv.set_channel(7)
    tv.show_status()


z16()