
# Feature Engineering Techniques in Python
## Merge Train and Test

    df = pd.concat([train[col],test[col]],axis=0)
    
## The label column will be set as NULL for test rows

## FEATURE ENGINEERING HERE
    train[col] = df[:len(train)]
    test[col] = df[len(train):]

## NAN trick
    df[col].fillna(-9999, inplace=True)

## Categorical Features
    df[col] = df[col].astype('category')

## Combining / Splitting

    new = df["localisation"].str.split("_", n = 1, expand = True)
    df['country'] = new[0]
    df['city']=new[1]

    df['zipcode'] = df['departement_code'].astype(str)+'_'+df['disctrict_code'].astype(str)
    

## Linear combinations
    
    df['area'] = df['width'] * df['height']


## Count column


## Deal with Date
    df['date'] =  pd.to_datetime(df[col], format='%d %b %Y')

    df['year'] =  df['date'].year
    df['month'] = df['date'].month
    df['day'] = df['date'].day


## Aggregations / Group Statistics

    temp = df.groupby('smartphone_brand')['call_duration']
           .agg(['mean'])
           .rename({'mean':'call_duration_mean'},axis=1)
    df = pd.merge(df,temp,on='smartphone_brand',how=’left’)


## Normalize / Standardize

    df[col] = ( df[col]-df[col].mean() ) / df[col].std()
    
    
    df[‘call_duration_remove_time’] = df[‘call_duration’] — df[‘call_duration_week_mean’] 
