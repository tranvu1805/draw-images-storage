# Urban ecosystem: Houston skyline above Sam Houston Park (public-domain photo, see ATTRIBUTION.md).
# The raw download is kept in work/downloads/img150/ (not in git); the committed jpg is the deliverable.
import os

from photo_kit import photo, _dk

photo('img150', os.path.join(_dk.WORK, 'downloads', 'img150', 'houston_skyline_1920.jpg'), crop=(0, 0.33, 1, 0.87))
