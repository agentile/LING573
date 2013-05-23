

config = {
    "search_libraries": ["pattern", "requests", "xgoogle"],
    "search_library_active": "pattern",
    "search_engines": ["bing", "google"],
    "search_engine_active": "google",
    "use_lucene_wildcard": True,
    "questions_to_answer":0,
    "aquant_index_dir": "aquaint_index",
    "web_cache_dir": "web_cache",
    "reset_web_cache": 0,
    "web_results_limit": 100,
    "answer_candidates_limit": 20,
    "include_exact_query_matches": 1,
    "deliverable": "D4",
    "trec_file": "/dropbox/12-13/573/Data/Questions/devtest/TREC-2006.xml",
    "binarize_cmd": "/NLP_TOOLS/tool_sets/mallet/latest/bin/mallet import-svmlight --input train.vectors.txt --output train.vectors",
    "train_cmd": "/NLP_TOOLS/tool_sets/mallet/latest/bin/mallet train-classifier --input train.vectors --trainer MaxEnt --output-classifier ml.model",
    "test_cmd": "/NLP_TOOLS/tool_sets/mallet/latest/bin/mallet classify-svmlight --input test.vectors.txt --output classifier.result --classifier ml.model"
}
