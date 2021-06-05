from models import Pet, db
from app import app

"""Create table"""
db.drop_all()
db.create_all()


pet1 = Pet(name="Golden", species="Golden Retriever", photo_url='https://assets.mydogsname.com/wp-content/uploads/2019/05/golden-retriever-breed.jpg',
           age='4', notes='Golden Retrievers make the ultimate family dog – they’re easy going, great with kids and other dogs, and do well with training. If you welcome this pup into your home, just remember they need lots of exercise and regular brushing', available=True)

pet2 = Pet(name="Charmer", species="Maltese", photo_url='https://assets.mydogsname.com/wp-content/uploads/2019/04/maltese-dog-breed.jpg',
           age='6 months', notes='is simply adorable. He packs in white fluffy fur, a black button nose and saucer-sized eyes into a tiny little body. Charming, playful and sweet, this pup brightens up any household.', available=False
           )

pet3 = Pet(name="Woolfy", species="German Shepherd", photo_url='https://assets.mydogsname.com/wp-content/uploads/2019/05/german-shepherd-breed.jpg',
           age='1', notes='this dog is great with children and other pups and does well with training. Just be sure he gets regular exercise and stimulation, and you’ll have the perfect pooch', available=True)

pet4 = Pet(name="Doll", species="Ragdoll", photo_url='https://uk.mypetandi.com/sites/g/files/adhwdz331/files/styles/paragraph_image/public/2018-03/ragdoll_cat_01401.jpg?itok=GLukk3cG',
           age='5 months', notes='the doll is a well-balanced cat with no extreme feature')


db.session.add_all([pet1, pet2, pet3, pet4])
db.session.commit()
