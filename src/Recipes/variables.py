#accidental cartesian join recipe
cartesian_join_dict = {'name':'Cartesian Join',
                       'description': """A Cartesian join occurs when a join condition is missing,
                           causing every row from one table to be paired with every row from another.
                           This results in an exponential number of rows, leading to performance issues.
                           to solve this, we'll add an ON clause where possible""",
                       'prompt': """You're a SQL query tuning expert. Sometimes people don't add an ON clause in their JOINs.
                             Change the query logic to use include ON statements in the JOINs without changing the query logic"""}

#union->union all recipe
union_change_dict = {'name':'Union->Union All',
                     'description':"""UNION ALL is a generaly more performative alternative to the 
                                        regular UNION command, so we will try to improv ethe run time by replacing UNION 
                                        with UNION ALL""",
                     'prompt': """Optimize the Union operations in this query by:

– Converting UNION to UNION ALL where duplicates are impossible

– Optimizing individual queries within the UNION"""}


#not exist->left join recipe
non_exist_to_left_dict = {'name':"",
                  'description':"""To solve cases of  non-existenet data, we can use LEFT JOIN to eliminate
                                                the problematic rows from the data and improve the runtime""",
                  'prompt': """optimize this query by
                             -Converting NOT EXISTS to LEFT JOIN with IS NULL check
                             -Maintaining correct NULL handling"""}

#pre-aggregation with cte recipe
cte_pre_agg_dict = {'name':"pre aggregation with CTEs",
                  'description':""".""",
                  'prompt': """Rewrite the SQL query to pre-aggregate data with a Commonn Table Expression(CTE) to improve performance"""}

#merge CTEs recipe
cte_merge_dict = {'name':"CTE merging",
                  'description':""".""",
                  'prompt': """You're a SQL query tuning expert. Sometimes people use too many CTEs.
                             Change the query logic to use less CTEs by merging CTEs that can be merged without changing the query logic"""}

#"Magic" recipe
magic_dict = {'name':"Magic",
              'description': """A general prompt to the LLM to rewrite the query as a 'veteran' SQL developer to optimize
                                the query""",
              'prompt': """You are a Senior Database Engineer. rewrite this SQL query to optimize performance by:
                         -Converting complex subqueries to efficient join operations
                         -Optimizing JOIN sequences for better performance
                         -Simplifying complex WHERE conditions
                         -Minimizing data movement between nodes where possible
                         -Improving GROUP BY and aggregation patterns
                         -Avoiding SELECT * and listing only needed columns"""}