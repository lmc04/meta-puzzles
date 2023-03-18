# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  # Keep track of a list where each element is a potential photograph.
  # That element will keep track of the the positions of items of a photograph
  # and what item it expects next (A after P, B after A, etc).
  # Since the same items can be used in multiple photograpgs (PAB, PA.B, etc),
  # existing potential photographs will not be updated, only new potential ones will
  # be created.
  photos = []
  for i in range(N):
    new_photos = []
    if C[i] == 'P':
      # Check if any potential photographs need a P.
      for photo in photos:
        # Only create new potential photographs if a P is needed in an existing one.
        if photo['needs'] == 'P':
          # Create a new potential photograph from the existing one.
          new_photo = dict(photo)
          # Set the position of P.
          new_photo['P'] = i
          # If the potential photograph needed a P, then that must mean
          # a B and A were already there, so it is now a complete photograph.
          new_photo['needs'] = 'complete'
          new_photos.append(new_photo)
      # Now that existing potential photographs have been checked, we can create
      # a new one because a photograph can start with P.
      new_photo = {}
      # Set the position of P.
      new_photo['P'] = i
      # Expecting an A next.
      new_photo['needs'] = 'A'
      new_photos.append(new_photo)
    # Repeat the same with a B.
    elif C[i] == 'B':
      for photo in photos:
        if photo['needs'] == 'B':
          new_photo = dict(photo)
          new_photo['B'] = i
          new_photo['needs'] = 'complete'
          new_photos.append(new_photo)
      new_photo = {}
      new_photo['B'] = i
      new_photo['needs'] = 'A'
      new_photos.append(new_photo)
    # Do a similar step with A.
    # The differences are that A cannot be the start of a photograph and what
    # is needed after A depends on which of P or B is already in the photograph.
    elif C[i] == 'A':
      for photo in photos:
        if photo['needs'] == 'A':
          new_photo = dict(photo)
          new_photo['A'] = i
          # These options are mutually exclusive because the photograph is not complete.
          if 'P' in photo:
            new_photo['needs'] = 'B'
          elif 'B' in photo:
            new_photo['needs'] = 'P'
          new_photos.append(new_photo)
    # '.' can be skipped because we keep track of the positions of the other items directly.
    # Add any new potential photographs to the set.
    photos.extend(new_photos)
  # Now that all cells have been stepped through, go through the potential photographs,
  # select the completed photographs, and see if they are artistic.
  artistic_total = 0
  for photo in photos:
    if photo['needs'] == 'complete':
      # Distance is the absolute value of the difference in position.
      PA_distance = abs(photo['P'] - photo['A'])
      BA_distance = abs(photo['B'] - photo['A'])
      # Artistic distance check, inclusive.
      if (X <= PA_distance <= Y) and (X <= BA_distance <= Y):
        artistic_total += 1
  return artistic_total
