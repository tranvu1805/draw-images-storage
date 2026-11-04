# Natural grassland ecosystem: bison herd grazing in Hayden Valley, Yellowstone (CC0 photo, see ATTRIBUTION.md).
# The raw download is kept in work/downloads/img149/ (not in git); the committed jpg is the deliverable.
import os

from photo_kit import photo, _dk

photo('img149', os.path.join(_dk.WORK, 'downloads', 'img149', 'hayden_valley_bison.jpg'), crop=(0, 0.17, 1, 1))
