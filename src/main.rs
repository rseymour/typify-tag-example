// Copyright 2023 Oxide Computer Company

use typify::import_types;

use serde::{Deserialize, Serialize};
// works with tag = "my_tag" annotation changed
//mod simple;
//use simple::MainModel;

import_types!(
    schema = "simple.json",
);

#[test]
fn test_main() {
    main()
}

fn main() {
    let data = r#"
        {
        "fbz":[{
            "my_type": "Baz",
            "count": 3
        }]}"#;

    let mm: MainModel = serde_json::from_str(data).unwrap();
// comes out as FooBar instead of Baz on my machine

    println!("{:?}", mm);
}
