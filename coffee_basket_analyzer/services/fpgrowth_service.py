import pandas as pd
from mlxtend.frequent_patterns import association_rules

class FpGrowthService:
    @staticmethod
    def id_to_name(df: pd.DataFrame, product_id: int) -> str:
        # Find label position
        for i, row in enumerate(df["itemsets"]):
            id_list = list(row)
            for j, id in enumerate(id_list):
                if product_id == int(id):
                    id_row = i
                    id_idx = j
        
        # Locate ID
        return df["labels"].iloc[id_row].split(",")[id_idx].strip()

    @staticmethod
    def name_to_id(df: pd.DataFrame, product_type: int) -> str:
        # Find label position
        for i, row in enumerate(df["labels"]):
            labels_list = row.split(",")
            for j, label in enumerate(labels_list):
                if product_type in label:
                    label_row = i
                    label_idx = j
        
        # Locate ID
        return int(list(df["itemsets"].iloc[label_row])[label_idx])
    
    @staticmethod
    def map_ids_to_names(distinct, x):
        label_list = [FpGrowthService.id_to_name(distinct, id) for id in list(x)]
        return label_list
            

    @staticmethod
    def LoadRules(itemsets, chosen_set, metric="confidence", threshold=0.5):
        rules_df = association_rules(itemsets, metric=metric, min_threshold=threshold)
        chosen_set = list([FpGrowthService.name_to_id(itemsets, item) for item in chosen_set])
        
        # Filter rules based on user input
        filtered_rules = rules_df[
            (rules_df["antecedents"].apply(lambda x: any(item in x for item in chosen_set)) |
            rules_df["consequents"].apply(lambda x: any(item in x for item in chosen_set)))
        ]

        filtered_rules["antecedents"] = filtered_rules["antecedents"].map(lambda x: FpGrowthService.map_ids_to_names(itemsets, x))
        filtered_rules["consequents"] = filtered_rules["consequents"].map(lambda x: FpGrowthService.map_ids_to_names(itemsets, x))

        return filtered_rules
