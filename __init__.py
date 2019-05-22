import numpy as np
import pandas as pd
import sqlalchemy as sqal
import progressbar as pb

widgets= pb.widgets([Percentage(), Bar()])
progress = pb.ProgressBar(widgets = widgets, maxval = 100).start()
progvar = 0

for i in range (100):
    engine = sqal.create_engine("sqlite:////media/sf_D_DRIVE/Datenbanken/caq_vw.sqlite3")

    df = pd.read_sql("SELECT * FROM arbeitsfolge_clean "
                "WHERE DATUM_UHRZEIT BETWEEN '2018-02-12 00:00:00' AND '2018-02-19 00:00:00' "
                "ORDER BY DATUM_UHRZEIT", engine)
    progress.update(progvar + 1)
    progvar += 1
    progress.finish()


