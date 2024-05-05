import os.path

from sqlalchemy import create_engine, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, sessionmaker

# Database engine object, deprecated in modern SQLAlchemy but still gets the job done
Base = declarative_base()

# Parameter class stores all parameters from every image ever generated.
# In SQLAlchemy, python objects can be treated as database objects, so language is interchangeable.
# In SQLAlchemy, columns at the top of the list are generated furthest to the left in the resultant database table.


class Parameter(Base):
    # Internal name for database
    __tablename__ = "parameters"

    filepath = mapped_column("filepath", String, primary_key=True)
    count_HL = mapped_column("count_HL", Integer)
    count_VL = mapped_column("count_VL", Integer)
    color_Dist = mapped_column("color_Dist", Integer)
    thick_L = mapped_column("thick_L", Integer)
    space_L = mapped_column("space_L", Integer)
    splitChance_HRect = mapped_column("splitChance_HRect", Integer)
    splitChance_VRect = mapped_column("splitChance_VRect", Integer)
    neighborColorChance = mapped_column("neighborColorChance", Integer)
    whiteRectChance = mapped_column("whiteRectChance", Integer)
    ratingGiven = mapped_column("ratingGiven", Integer, ForeignKey("average-ratings.ratingGiven"))

    # Dictionary of Columns
    # filepath is the location of the image in the working directory
    # filepath is the primary key for the Parameter Class
    # count_HL is the horizontal line count
    # count_VL is the vertical line count
    # color_Dist is the color distancing
    # thick_L is the line thickness
    # space_L is the line spacing
    # splitChance_HRect is the chance a rectangle object forms between horizontal lines
    # splitChance_VRect is the chance a rectangle object forms between vertical lines
    # neighborColorChance is the chance neighboring rectangles have differing colors
    # whiteRectChance is the chance a rectangle will be the color white
    # ratingGiven is the rating that the AI determines for the image
    # ratingGiven is the foreign key to rating in the AverageRating class
    # End Dictionary of Columns

    # Database table initialization method
    def __init__(self, filepath, count_HL, count_VL, color_Dist, thick_L, space_L, splitChance_HRect, splitChance_VRect,
                 neighborColorChance, whiteRectChance, ratingGiven):
        self.filepath = filepath
        self.count_HL = count_HL
        self.count_VL = count_VL
        self.color_Dist = color_Dist
        self.thick_L = thick_L
        self.space_L = space_L
        self.splitChance_HRect = splitChance_HRect
        self.splitChance_VRect = splitChance_VRect
        self.neighborColorChance = neighborColorChance
        self.whiteRectChance = whiteRectChance
        self.ratingGiven = ratingGiven

    # Database session commit method
    def __repr__(self):
        return (f"({self.filepath}) {self.count_HL} {self.count_VL} {self.thick_L} {self.color_Dist} {self.space_L} "
                f"{self.splitChance_HRect} {self.splitChance_VRect} {self.neighborColorChance} {self.whiteRectChance} "
                f"{self.ratingGiven} ")

# Averages class takes the average of the parameters of every image within a certain "interval"
# Interval means that ratings are truncated down to base 10
# Example of finding an interval: If rating of 19 in Parameters, averages will be calculated in the interval "10"
# There are 11 intervals, numbering from 0 to 11.
# Each interval has an "equation key":
# eq_#S is a foreign key link to the Sums Class
# eq_#T is a foreign key link to the Totals Class


class AverageRating(Base):
    # Internal name for database
    __tablename__ = "average-ratings"

    rating = mapped_column("ratingGiven", Integer, primary_key=True)
    avg_count_HL = mapped_column("avg_count_HL", Integer)
    avg_count_VL = mapped_column("avg_count_VL", Integer)
    avg_color_Dist = mapped_column("avg_color_Dist", Integer)
    avg_thick_L = mapped_column("avg_thick_L", Integer)
    avg_space_L = mapped_column("avg_space_L", Integer)
    avg_splitChance_HRect = mapped_column("avg_splitChance_HRect", Integer)
    avg_splitChance_VRect = mapped_column("avg_splitChance_VRect", Integer)
    avg_neighborColorChance = mapped_column("avg_neighborColorChance", Integer)
    avg_whiteRectChance = mapped_column("avg_whiteRectChance", Integer)
    prev_Total_Key = mapped_column("prev_Total_Key", String, ForeignKey("total-parameters.prev_Total"))
    sum_Entries_Key = mapped_column("sum_Entries_Key", String, ForeignKey("sum-parameters.sum_Entries"))

    # Start Dictionary of Columns
    # rating has the same meaning as the rating in the Parameter class
    # rating is primary key from the foreign key in the Parameter class
    # all parameters have the same meaning but maintain the prefix "avg_" for differentiation
    # prev_Total_Key is the equation key for the Totals Class
    # prev_Total_Key is the foreign key for the Totals Class
    # sum_Entries_Key is the equation key for the Sums Class
    # sum_Entries_Key is the equation key for the Sums Class
    # End Dictionary of Columns

    # Database table initialization method
    def __init__(self, rating, count_HL, count_VL, color_Dist, thick_L, space_L, splitChance_HRect, splitChance_VRect,
                 neighborColorChance, whiteRectChance, prev_Total_Key, sum_Entries_Key):
        self.rating = rating
        self.avg_count_HL = count_HL
        self.avg_count_VL = count_VL
        self.avg_color_Dist = color_Dist
        self.avg_thick_L = thick_L
        self.avg_space_L = space_L
        self.avg_splitChance_HRect = splitChance_HRect
        self.avg_splitChance_VRect = splitChance_VRect
        self.avg_neighborColorChance = neighborColorChance
        self.avg_whiteRectChance = whiteRectChance
        self.prev_Total_Key = prev_Total_Key
        self.sum_Entries_Key = sum_Entries_Key

    # Database session commit method
    def __repr__(self):
        return (f"({self.rating}) {self.avg_count_HL} {self.avg_count_VL} {self.avg_thick_L} {self.avg_color_Dist} "
                f"{self.avg_space_L} {self.avg_splitChance_HRect} {self.avg_splitChance_VRect} "
                f"{self.avg_neighborColorChance} {self.avg_whiteRectChance} {self.prev_Total_Key} "
                f"{self.sum_Entries_Key} ")

    # Because there are a set amount of intervals, this method generates the intervals as 11 rows.
    def init_averages(self):
        avgSession = averageSession()     # Start database session

        # For loop to generate each row with rating, each parameter (as a 0) in order, and equation keys
        j = 100
        for i in range(11):
            parameters = AverageRating(j, 0, 0, 0, 0, 0, 0, 0, 0, 0, "eq" + str(int(j/10))
                                       + "_T", "eq" + str(int(j/10)) + "_S")
            j -= 10
            avgSession.add(parameters)

        avgSession.commit()  # End database access

    # Simple method which rounds ratings down into intervals
    def truncate(rating):
        truncated = int(rating)
        return truncated

    # This method updates the AverageRating Class, SumParameter Class, and the TotalParameter Class
    # This method only occurs when a new image is generated.
    def update_averages(rating, count_HL, count_VL, color_Dist, thick_L, space_L, splitChance_HRect, splitChance_VRect,
                        neighborColorChance, whiteRectChance):
        avgSession = averageSession()   # start database session x3
        sSession = sumSession()
        totSession = totalSession()

        # Find the row in AverageRating Class to update given the truncated rating
        updateAveragesRow = avgSession.query(AverageRating).filter(AverageRating.rating == int(rating)).first()
        # Find the row in SumParameter Class to update given the corresponding equation key
        updateSumsRow = (sSession.query(SumParameter)
                         .filter(SumParameter.sum_Entries == "eq" + str(int(rating/10)) + "_S")).first()
        # Find the row in TotalParameter Class to update given the corresponding equation key
        updateTotalsRow = (totSession.query(TotalParameter)
                           .filter(TotalParameter.prev_Total == "eq" + str(int(rating/10)) + "_T")).first()

        # FOR EACH PARAMETER:
        # If this is the first time adding to the class AverageRating table, the previous sum will be 0.
        # Therefore, the average is just the parameter itself.
        # Otherwise, the average is the ((parameter + existing) / previous-total).

        # Horizontal Line Count Rows
        if updateSumsRow.sum_count_HL == 0:
            updateAveragesRow.avg_count_HL = count_HL
        else:
            updateAveragesRow.avg_count_HL = (count_HL + updateSumsRow.sum_count_HL / updateTotalsRow.prev_count_HL)

        updateSumsRow.sum_count_HL += count_HL
        updateTotalsRow.prev_count_HL += 1
        print("*** Updated Horizontal Line Averages for rating " + str(int(rating)))

        # Vertical Line Count Rows
        if updateSumsRow.sum_count_VL == 0:
            updateAveragesRow.avg_count_VL = count_VL
        else:
            updateAveragesRow.avg_count_VL = (count_VL + updateSumsRow.sum_count_HL / updateTotalsRow.prev_count_VL)

        updateSumsRow.sum_count_VL += count_VL
        updateTotalsRow.prev_count_VL += 1
        print("*** Updated Vertical Line Averages for rating " + str(int(rating)))

        # Color Distance Rows
        if updateSumsRow.sum_color_Dist == 0:
            updateAveragesRow.avg_color_Dist = color_Dist
        else:
            updateAveragesRow.avg_color_Dist = \
                (color_Dist + updateSumsRow.sum_color_Dist / updateTotalsRow.prev_color_Dist)

        updateSumsRow.sum_color_Dist += color_Dist
        updateTotalsRow.prev_color_Dist += 1
        print("*** Updated Color Distance Averages for rating " + str(int(rating)))

        # Line Thickness Rows
        if updateSumsRow.sum_thick_L == 0:
            updateAveragesRow.avg_thick_L = thick_L
        else:
            updateAveragesRow.avg_thick_L = (thick_L + updateSumsRow.sum_thick_L) / updateTotalsRow.prev_thick_L

        updateSumsRow.sum_thick_L += thick_L
        updateTotalsRow.prev_thick_L += 1
        print("*** Updated Line Thickness Averages for rating " + str(int(rating)))

        # Line Spacing Rows
        if updateSumsRow.sum_space_L == 0:
            updateAveragesRow.avg_space_L = space_L
        else:
            updateAveragesRow.avg_space_L = (space_L + updateSumsRow.sum_space_L) / updateTotalsRow.prev_space_L

        updateSumsRow.sum_space_L += space_L
        updateTotalsRow.prev_space_L += 1
        print("*** Updated Line Spacing Averages for rating " + str(int(rating)))

        # Split Chance Horizontal Rectangle Rows
        if updateSumsRow.sum_splitChance_HRect == 0:
            updateAveragesRow.avg_splitChance_HRect = splitChance_HRect
        else:
            updateAveragesRow.avg_splitChance_HRect = \
                (splitChance_HRect + updateSumsRow.sum_splitChance_HRect) / updateTotalsRow.prev_splitChance_HRect

        updateSumsRow.sum_splitChance_HRect += splitChance_HRect
        updateTotalsRow.prev_splitChance_HRect += 1
        print("*** Updated Split Chance Horizontal Rectangles for rating " + str(int(rating)))

        # Split Chance Vertical Rectangle Rows
        if updateSumsRow.sum_splitChance_VRect == 0:
            updateAveragesRow.avg_splitChance_VRect = splitChance_VRect
        else:
            updateAveragesRow.avg_splitChance_VRect = \
                (splitChance_VRect + updateSumsRow.sum_splitChance_VRect) / updateTotalsRow.prev_splitChance_VRect

        updateSumsRow.sum_splitChance_VRect += splitChance_VRect
        updateTotalsRow.prev_splitChance_VRect += 1
        print("*** Updated Split Chance Vertical Rectangles for rating " + str(int(rating)))

        # Neighbor Color Chance Rows
        if updateSumsRow.sum_neighborColorChance == 0:
            updateAveragesRow.avg_neighborColorChance = neighborColorChance
        else:
            updateAveragesRow.avg_neighborColorChance = \
                (neighborColorChance + updateSumsRow.sum_neighborColorChance) / updateTotalsRow.prev_neighborColorChance

        updateSumsRow.sum_neighborColorChance += neighborColorChance
        updateTotalsRow.prev_neighborColorChance += 1
        print("*** Updated Neighbor Color Chance for rating " + str(int(rating)))

        # White Rectangle Chance Rows
        if updateSumsRow.sum_whiteRectChance == 0:
            updateAveragesRow.avg_whiteRectChance = whiteRectChance
        else:
            updateAveragesRow.avg_whiteRectChance = \
                (whiteRectChance + updateSumsRow.sum_whiteRectChance) / updateTotalsRow.prev_whiteRectChance

        updateSumsRow.sum_whiteRectChance += whiteRectChance
        updateTotalsRow.prev_whiteRectChance += 1
        print("*** Updated White Rectangle Chance for rating " + str(int(rating)))

        avgSession.commit()     # End database access x3
        sSession.commit()
        totSession.commit()

        avgSession.commit()

# SumParameter Class stores the collective numerator for each parameter of all the AverageRating Class intervals.
# Common numerators are stored only when an image is generated.


class SumParameter(Base):
    # Internal name for database
    __tablename__ = "sum-parameters"

    sum_Entries = mapped_column("sum_Entries", String, primary_key=True)
    sum_count_HL = mapped_column("sum_count_HL", Integer)
    sum_count_VL = mapped_column("sum_count_VL", Integer)
    sum_color_Dist = mapped_column("sum_color_Dist", Integer)
    sum_thick_L = mapped_column("sum_thick_L", Integer)
    sum_space_L = mapped_column("sum_space_L", Integer)
    sum_splitChance_HRect = mapped_column("sum_splitChance_HRect", Integer)
    sum_splitChance_VRect = mapped_column("sum_splitChance_VRect", Integer)
    sum_neighborColorChance = mapped_column("sum_neighborColorChance", Integer)
    sum_whiteRectChance = mapped_column("sum_whiteRectChance", Integer)

    # Start Dictionary of Columns
    # sum_Entries is the primary key of the SumParameter Class
    # sum_Entries is the equation key of the SumParameter Class
    # all parameters have the same meaning but maintain the prefix "sum_" for differentiation
    # No foreign keys in this table
    # End Dictionary of Columns

    # Database table initialization method
    def __init__(self, sum_Entries, sum_count_HL, sum_count_VL, sum_color_Dist, sum_thick_L, sum_space_L,
                 sum_splitChance_HRect, sum_splitChance_VRect, sum_neighborColorChance, sum_WhiteRectChance):
        self.sum_Entries = sum_Entries
        self.sum_count_HL = sum_count_HL
        self.sum_count_VL = sum_count_VL
        self.sum_color_Dist = sum_color_Dist
        self.sum_thick_L = sum_thick_L
        self.sum_space_L = sum_space_L
        self.sum_splitChance_HRect = sum_splitChance_HRect
        self.sum_splitChance_VRect = sum_splitChance_VRect
        self.sum_neighborColorChance = sum_neighborColorChance
        self.sum_whiteRectChance = sum_WhiteRectChance


    # Database session commit method
    def __repr__(self):
        return(f"({self.sum_Entries}) {self.sum_count_HL} {self.sum_count_VL} {self.sum_color_Dist} {self.sum_thick_L} "
               f"{self.sum_space_L} {self.sum_splitChance_HRect} {self.sum_splitChance_VRect} "
               f"{self.sum_neighborColorChance} {self.sum_whiteRectChance}")

    # Because there are a set amount of intervals, this method generates the intervals as 10 rows.
    def init_sums(self):
        sSession = sumSession()     # Start database session

        # For loop to generate each row with equation key and each parameter (as a 0) in order
        j = 100
        for i in range(11):
            parameters = SumParameter("eq" + str(i) + "_S", 0, 0, 0, 0, 0, 0, 0, 0, 0)
            j -= 10
            sSession.add(parameters)

        sSession.commit()  # End database access

# TotalParameter Class stores the collective denominator for each parameter of all the AverageRating Class intervals.
# Common denominators are stored only when an image is generated.


class TotalParameter(Base):
    # Internal name for database
    __tablename__ = "total-parameters"

    prev_Total = mapped_column("prev_Total", String, primary_key=True)
    prev_count_HL = mapped_column("prev_count_HL", Integer)
    prev_count_VL = mapped_column("prev_count_VL", Integer)
    prev_color_Dist = mapped_column("prev_color_Dist", Integer)
    prev_thick_L = mapped_column("prev_thick_L", Integer)
    prev_space_L = mapped_column("prev_space_L", Integer)
    prev_splitChance_HRect = mapped_column("prev_splitChance_HRect", Integer)
    prev_splitChance_VRect = mapped_column("prev_splitChance_VRect", Integer)
    prev_neighborColorChance = mapped_column("prev_neighborColorChance", Integer)
    prev_whiteRectChance = mapped_column("prev_whiteRectChance", Integer)

    # Start Dictionary of Columns
    # prev_Total is the primary key of the TotalParameter Class
    # prev_Total is the equation key of the TotalParameter Class
    # all parameters have the same meaning but maintain the prefix "prev_" for differentiation
    # No foreign keys in this table
    # End Dictionary of Columns

    # Database table initialization method
    def __init__(self, prev_Total, prev_count_HL, prev_count_VL, prev_color_Dist, prev_thick_L, prev_space_L,
                 prev_splitChance_HRect, prev_splitChance_VRect, prev_neighborColorChance, prev_whiteRectChance):
        self.prev_Total = prev_Total
        self.prev_count_HL = prev_count_HL
        self.prev_count_VL = prev_count_VL
        self.prev_color_Dist = prev_color_Dist
        self.prev_thick_L = prev_thick_L
        self.prev_space_L = prev_space_L
        self.prev_splitChance_HRect = prev_splitChance_HRect
        self.prev_splitChance_VRect = prev_splitChance_VRect
        self.prev_neighborColorChance = prev_neighborColorChance
        self.prev_whiteRectChance = prev_whiteRectChance

    # Database session commit method
    def __repr__(self):
        return (f"({self.prev_Total}) {self.prev_count_HL} {self.prev_count_VL} {self.prev_color_Dist} "
                f"{self.prev_thick_L} {self.prev_space_L} {self.prev_splitChance_HRect} {self.prev_splitChance_VRect} "
                f"{self.prev_neighborColorChance} {self.prev_whiteRectChance}")

    # Because there are a set amount of intervals, this method generates the intervals as 10 rows.
    def init_totals(self):
        totSession = totalSession()     # Start database session

        # For loop to generate each row with equation key and each parameter (as a 0) in order
        j = 100
        for i in range(11):
            parameters = TotalParameter("eq" + str(i) + "_T", 0, 0, 0, 0, 0, 0, 0, 0, 0)
            j -= 10
            totSession.add(parameters)

        totSession.commit()  # End database access

# Start DAO Objects


parameterEngine = create_engine("sqlite:///parameters.db", echo=True)     # Engine to base session for parameters.db
Base.metadata.create_all(bind=parameterEngine)                            # create parameters.db base

parameterSession = sessionmaker(bind=parameterEngine)                     # Session to access parameters.db

averageEngine = create_engine("sqlite:///average-ratings.db", echo=True)  # Engine->base session for average-ratings.db
Base.metadata.create_all(bind=averageEngine)                              # create average-ratings.db base

averageSession = sessionmaker(bind=averageEngine)                         # Session to access average-ratings.db

sumEngine = create_engine("sqlite:///sum-parameters.db")                  # Engine->base session for sum-parameters.db
Base.metadata.create_all(bind=sumEngine)                                  # create sum-parameters.db base

sumSession = sessionmaker(bind=sumEngine)                                 # Session to access sum-parameters.db

totalEngine = create_engine("sqlite:///total-parameters.db")              # Engine->base session for total-parameters.db
Base.metadata.create_all(bind=totalEngine)                                # create total-parameters.db base

totalSession = sessionmaker(bind=totalEngine)                             # Session to access total-parameters.db

if not os.path.exists("db_initialized.txt"):                              # Initialize tables if db_initialized.txt DNE.
    AverageRating.init_averages(1)                                        # The database tables always exist, cannot use
    SumParameter.init_sums(1)                                             # the path for a database file as a check to
    TotalParameter.init_totals(1)                                         # initialize them.

    with open('db_initialized.txt', 'w') as f:
        f.write('Successfully Initialized AverageRating, SumParameter, TotalParameter!')
# End DAO Objects