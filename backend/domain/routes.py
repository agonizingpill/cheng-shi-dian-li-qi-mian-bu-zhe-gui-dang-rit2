from domain.flag_archive_api import router as flag_archive
from domain.crease_samples_api import router as crease_samples
from domain.fold_exemplars_api import router as fold_exemplars
from domain.storage_slips_api import router as storage_slips

routers = (flag_archive, crease_samples, fold_exemplars, storage_slips,)
