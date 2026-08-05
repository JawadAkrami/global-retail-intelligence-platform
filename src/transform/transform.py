

before = len(df)

df = df.drop_duplicates()

after = len(df)

logger.info(
    f"{name}: removed {before - after} duplicate rows"
)