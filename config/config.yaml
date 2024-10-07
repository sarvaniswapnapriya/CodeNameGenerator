# config/config.yaml

default: &default
  app_name: "Random Code Name Generator"
  debug: true
  database:
    uri: "sqlite:///dev_code_names.db"

development:
  <<: *default
  environment: "development"
  database:
    uri: "sqlite:///dev_code_names.db"

production:
  <<: *default
  environment: "production"
  debug: false
  database:
    uri: "sqlite:///prod_code_names.db"
