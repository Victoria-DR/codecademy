import datetime

class Art:
  def __init__(self, artist, title, year, medium, owner):
    self.artist = artist
    self.title = title
    self.year = year
    self.medium = medium
    self.owner = owner

  def __repr__(self):
    return f"{self.artist}. \"{self.title}\". {self.year}, {self.medium}. {self.owner.name}, {self.owner.location}."

class Marketplace:
  def __init__(self):
    self.listings = []

  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, old_listing):
    self.listings.remove(old_listing)

  def show_listings(self):
    for listing in self.listings:
      if listing.expiration_date < datetime.date.today():
        remove_listing(listing)
      else:
        print(listing)

# veneer = Marketplace()

class Client:
  def __init__(self, name, location, is_museum, wallet, wishlist):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    self.wallet = wallet
    self.wishlist = wishlist

  def sell_artwork(self, artwork, price, expiration_date):
    if artwork.owner == self:
      veneer.add_listing(Listing(artwork, price, self, expiration_date))

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      for listing in veneer.listings:

        if artwork == listing.art:
          art_listing = artwork

          if listing.expiration_date < datetime.date.today():
            veneer.remove_listing(listing)
            print("Listing unavailable.")
            break

          artwork.owner.wallet += listing.price
          self.wallet -= listing.price

          artwork.owner = self
          veneer.remove_listing(listing)

          break

class Listing:
  def __init__(self, art, price, seller, expiration_date):
    self.art = art
    self.price = price
    self.seller = seller
    self.expiration_date = expiration_date

  def __repr__(self):
    return f"{self.art.title}, {self.price}."

# edytta = Client("Edytta Halpirt", "Private Collection", False, 10000000, None)
# moma = Client("The MOMA", "New York", True, 600000000, None)

# girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)

# edytta.sell_artwork(girl_with_mandolin, 6000000, datetime.date(2020, 12, 19))
# moma.buy_artwork(girl_with_mandolin)

# print(girl_with_mandolin)
# veneer.show_listings()
