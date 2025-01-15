
udit@DESKTOP-FG5GVUC:/mnt/d/Github/CodeCrafters/codecrafters-kafka-python$ gp
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 177 bytes | 22.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
remote: ------------------------------------------------------------------------
remote:
remote:
remote:      ___            _          ___              __  _
remote:     / __\ ___    __| |  ___   / __\_ __  __ _  / _|| |_  ___  _ __  ___
remote:    / /   / _ \  / _` | / _ \ / /  | '__|/ _` || |_ | __|/ _ \| '__|/ __|
remote:   / /___| (_) || (_| ||  __// /___| |  | (_| ||  _|| |_|  __/| |   \__
remote:   \____/ \___/  \__,_| \___|\____/|_|   \__,_||_|   \__|\___||_|   |___/
remote:
remote:
remote:    Welcome to CodeCrafters! Your commit was received successfully.
remote:
remote: ------------------------------------------------------------------------
remote:
remote: ⚡ This is a turbo test run. https://codecrafters.io/turbo
remote:
remote: Running tests on your code. Logs should appear shortly...
remote:
remote: [compile] Moved ./.codecrafters/run.sh → ./your_program.sh
remote: [compile] Compilation successful.
remote:
remote: Debug = true
remote:
remote: [tester::#NH4] Running tests for Stage #NH4 (Concurrent Clients - Serial requests)
remote: [tester::#NH4] $ ./your_program.sh /tmp/server.properties
remote: [tester::#NH4] Connecting to broker at: localhost:9092
remote: [your_program] Logs from your program will appear here!
remote: [tester::#NH4] Connection to broker at localhost:9092 successful
remote: [tester::#NH4] Sending request 1 of 3: "ApiVersions" (version: 4) request (Correlation id: 342314397)
remote: [tester::#NH4] Hexdump of sent "ApiVersions" request:
remote: [tester::#NH4] Idx  | Hex                                             | ASCII
remote: [tester::#NH4] -----+-------------------------------------------------+-----------------
remote: [tester::#NH4] 0000 | 00 00 00 23 00 12 00 04 14 67 4d 9d 00 09 6b 61 | ...#.....gM...ka
remote: [tester::#NH4] 0010 | 66 6b 61 2d 63 6c 69 00 0a 6b 61 66 6b 61 2d 63 | fka-cli..kafka-c
remote: [tester::#NH4] 0020 | 6c 69 04 30 2e 31 00                            | li.0.1.
remote: [tester::#NH4]
remote: [tester::#NH4] Hexdump of received "ApiVersions" response:
remote: [tester::#NH4] Idx  | Hex                                             | ASCII
remote: [tester::#NH4] -----+-------------------------------------------------+-----------------
remote: [tester::#NH4] 0000 | 00 00 00 13 14 67 4d 9d 00 00 02 00 12 00 00 00 | .....gM.........
remote: [tester::#NH4] 0010 | 04 00 00 00 00 00 00                            | .......
remote: [tester::#NH4]
remote: [tester::#NH4] [Decoder] - .ResponseHeader
remote: [tester::#NH4] [Decoder]   - .correlation_id (342314397)
remote: [tester::#NH4] [Decoder] - .ResponseBody
remote: [tester::#NH4] [Decoder]   - .error_code (0)
remote: [tester::#NH4] [Decoder]   - .num_api_keys (1)
remote: [tester::#NH4] [Decoder]   - .ApiKeys[0]
remote: [tester::#NH4] [Decoder]     - .api_key (18)
remote: [tester::#NH4] [Decoder]     - .min_version (0)
remote: [tester::#NH4] [Decoder]     - .max_version (4)
remote: [tester::#NH4] [Decoder]     - .TAG_BUFFER
remote: [tester::#NH4] [Decoder]   - .throttle_time_ms (0)
remote: [tester::#NH4] [Decoder]   - .TAG_BUFFER
remote: [tester::#NH4] ✓ Correlation ID: 342314397
remote: [tester::#NH4] ✓ Error code: 0 (NO_ERROR)
remote: [tester::#NH4] ✓ API keys array is non-empty
remote: [tester::#NH4] ✓ API version 4 is supported for API_VERSIONS
remote: [tester::#NH4] ✓ Test 1 of 3: Passed
remote: [tester::#NH4] Sending request 2 of 3: "ApiVersions" (version: 4) request (Correlation id: 1636350266)
remote: [tester::#NH4] Hexdump of sent "ApiVersions" request:
remote: [tester::#NH4] Idx  | Hex                                             | ASCII
remote: [tester::#NH4] -----+-------------------------------------------------+-----------------
remote: [tester::#NH4] 0000 | 00 00 00 23 00 12 00 04 61 88 b9 3a 00 09 6b 61 | ...#....a..:..ka
remote: [tester::#NH4] 0010 | 66 6b 61 2d 63 6c 69 00 0a 6b 61 66 6b 61 2d 63 | fka-cli..kafka-c
remote: [tester::#NH4] 0020 | 6c 69 04 30 2e 31 00                            | li.0.1.
remote: [tester::#NH4]
remote: [tester::#NH4] EOF
remote: [tester::#NH4] Test failed
remote: [tester::#NH4] Terminating program
remote: [your_program] KafkaRequest(msg_size=35, api_key=18, api_version=4, correlation_id=342314397)
remote: [tester::#NH4] Program terminated successfully
remote:
remote: Try our CLI to run tests faster without Git: https://codecrafters.io/cli
remote:
remote: View our article on debugging test failures: https://codecrafters.io/debug
remote:
To https://git.codecrafters.io/e24031ac31ff2028
   eb9e2a4..2541335  master -> master