"""True values to check against."""

# True values after importing basic_import_test.bel.json with only extension - test_import_json
NODES_EXTENSION = {
    "bel": 12,
    "nn": 12,
    "pure_object": 11,
    "location_object": 10,
    "bio_concept": 0,
    "biological_process": 0,
    "pathology": 0,
    "bio_object": 11,
    "complex": 0,
    "abundance": 1,
    "population": 0,
    "genetic_flow": 10,
    "gene": 4,
    "rna": 3,
    "protein": 3,
    "micro_rna": 0,
    "bio_act": 1,
    "activity": 1,
    "reaction": 0,
    "degradation": 0,
    "cell_secretion": 0,
    "translocation": 0,
    "cell_surface_expression": 0,
    "bio_list": 0,
    "list": 0,
    "composite": 0,
    "ebel": 0,
    "variant": 0,
    "fragment": 0,
    "location": 0,
    "pmod": 0,
    "gmod": 0,
    "from_location": 0,
    "to_location": 0,
    "reactants": 0,
    "products": 0,
    "fusion_protein": 0,
    "fusion_rna": 0,
    "fusion_gene": 0,
}
EDGES_EXTENSION = {
    "bel_relation": 9,
    "causal": 3,
    "increases": 1,
    "directly_increases": 1,
    "decreases": 1,
    "directly_decreases": 0,
    "rate_limiting_step_of": 0,
    "causes_no_change": 0,
    "regulates": 0,
    "correlative": 0,
    "negative_correlation": 0,
    "positive_correlation": 0,
    "association": 0,
    "no_correlation": 0,
    "genomic": 6,
    "orthologous": 0,
    "transcribed_to": 3,
    "translated_to": 3,
    "other": 0,
    "has_member": 0,
    "has_members": 0,
    "has_component": 0,
    "has_components": 0,
    "equivalent_to": 0,
    "is_a": 0,
    "sub_process_of": 0,
    "deprecated": 0,
    "analogous_to": 0,
    "biomarker_for": 0,
    "prognostic_biomarker_for": 0,
    "compiler": 0,
    "acts_in": 0,
    "has_product": 0,
    "has_variant": 0,
    "has_modification": 0,
    "reactant_in": 0,
    "translocates": 0,
    "includes": 0,
    "ebel_relation": 1,
    "has__protein": 1,
    "has__rna": 0,
    "has__gene": 0,
    "has__abundance": 0,
    "has__population": 0,
    "has__location": 0,
    "has__from_location": 0,
    "has__to_location": 0,
    "has__fragment": 0,
    "has__pmod": 0,
    "has__gmod": 0,
    "has__complex": 0,
    "has__micro_rna": 0,
    "has__variant": 0,
    "has__reactants": 0,
    "has__products": 0,
    "has__composite": 0,
    "has_fragmented_protein": 0,
    "has_modified": 0,
    "has_modified_protein": 0,
    "has_modified_gene": 0,
    "has_variant_obj": 0,
    "has_variant_gene": 0,
    "has_variant_rna": 0,
    "has_variant_protein": 0,
    "has_variant_micro_rna": 0,
    "has_located": 0,
    "has_located_gene": 0,
    "has_located_rna": 0,
    "has_located_protein": 0,
    "has_located_micro_rna": 0,
    "has_located_complex": 0,
    "has_located_abundance": 0,
    "has_located_population": 0,
    "pathway_interaction": 0,
    "has_ppi": 0,
}
