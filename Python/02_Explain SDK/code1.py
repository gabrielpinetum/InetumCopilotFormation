df['new_column'] = df.apply(lambda row: [model.predict([row[col]]) for col in ['col1', 'col2', 'col3']], axis=1)