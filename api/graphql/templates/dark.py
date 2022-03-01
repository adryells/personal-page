GRAPHQL_HTML = """
<!DOCTYPE html>
<html>

<head>
    <title>GraphiQL</title>
    <style>
        html,
        body {
            height: 100%;
            margin: 0;
            overflow: hidden;
            width: 100%;
        }

        #graphiql {
            height: 100vh;
        }
    </style>

    <link rel="stylesheet"
        href="https://unpkg.com/graphiql-with-extensions@0.14.3/graphiqlWithExtensions.css"
        integrity="sha384-GBqwox+q8UtVEyBLBKloN5QDlBDsQnuoSUfMeJH1ZtDiCrrk103D7Bg/WjIvl4ya" crossorigin="anonymous" />
    <script src="https://unpkg.com/whatwg-fetch@2.0.3/fetch.js"
        integrity="sha384-KaKx4aJnrltBb2dne61B/MRPA4uRfQvv6YW99RgjHax8TRjFxcC4BC19EEX0te/6"
        crossorigin="anonymous"></script>
    <script src="https://unpkg.com/react@16.8.6/umd/react.production.min.js"
        integrity="sha384-qn+ML/QkkJxqn4LLs1zjaKxlTg2Bl/6yU/xBTJAgxkmNGc6kMZyeskAG0a7eJBR1"
        crossorigin="anonymous"></script>
    <script src="https://unpkg.com/react-dom@16.8.6/umd/react-dom.production.min.js"
        integrity="sha384-85IMG5rvmoDsmMeWK/qUU4kwnYXVpC+o9hoHMLi4bpNR+gMEiPLrvkZCgsr7WWgV"
        crossorigin="anonymous"></script>
    <script src="https://unpkg.com/graphiql-with-extensions@0.14.3/graphiqlWithExtensions.min.js"
        integrity="sha384-TqI6gT2PjmSrnEOTvGHLad1U4Vm5VoyzMmcKK0C/PLCWTnwPyXhCJY6NYhC/tp19"
        crossorigin="anonymous"></script>
    <script src="https://unpkg.com/js-cookie@3.0.0-rc.2/dist/js.cookie.umd.min.js"></script>

    <!-- breaking changes in subscriptions-transport-ws since 0.9.0 -->
    <script src="https://unpkg.com/subscriptions-transport-ws@0.8.3/browser/client.js"></script>
    <script src="https://unpkg.com/graphiql-subscriptions-fetcher@0.0.2/browser/client.js"></script>
    <style>

     .CodeMirror {
      background: #282d34 !important;
    }
    .graphiql-container .doc-explorer-contents,
    .graphiql-container .history-contents {
      background-color: #21262b;
      border-top: 1px solid #181a1f;
    }

    .graphiql-container .toolbar-button {
      background: #1c2125 !important;
      box-shadow: none !important;
      color: #5c626d !important;
      border: 1px solid #181a1f !important;
    }

    .graphiql-container .result-window .CodeMirror-gutters {
      background: #282d33;
      border: none !important;
    }

    .graphiql-container .resultWrap {
      border-left: solid 1px #181a1f;
    }

    .graphiql-container .variable-editor-title {
      background: #21262b;
      border-bottom: 1px solid #181a1f;
      border-top: 1px solid #181a1f;
      color: #cacdd3;
    }

    .graphiql-container .topBar {
      background: #21262b;
      border-color: #181a1f;
    }

    .graphiql-container .docExplorerHide {
      color: #606671;
    }

    .graphiql-container .doc-explorer-title,
    .graphiql-container .history-title,
    .doc-explorer-back {
      color: #cacdd3 !important;
    }

    .graphiql-container .doc-explorer {
      background: #21262b;
    }

    .graphiql-container .docExplorerWrap,
    .graphiql-container .historyPaneWrap {
      box-shadow: none;
    }

    .graphiql-container .docExplorerShow {
      border-left: none;
    }
    .graphiql-container .docExplorerShow,
    .graphiql-container .historyShow {
      background: #21262b;
      border-bottom: 1px solid #181a1e;
      color: #cacdd3;
    }

    .graphiql-container .docExplorerShow:before,
    .graphiql-container .doc-explorer-back:before {
      border-color: #cacdd3;
    }

    .graphiql-container .search-box {
      margin: auto auto 10px auto;
      border: none;
    }
    .graphiql-container .search-box input {
      background: #1e2127;
      padding-left: 28px;
    }

    .graphiql-container .search-box .search-box-clear,
    .graphiql-container .search-box .search-box-clear:hover {
      background: #1d2126;
    }

    .graphiql-container .search-box:before {
      color: #c1c4ca;
      font-size: 21px;
      left: 8px;
    }

    .graphiql-container,
    .graphiql-container button,
    .graphiql-container input {
      color: #9299a7;
    }

    .CodeMirror-gutters {
      border: none !important;
      background-color: #282d33;
    }

    .graphiql-container .execute-button {
      background: #21262b;
      border: 1px solid rgb(91, 98, 107);
      box-shadow: none !important;
      fill: #c9ccd2;
    }

    .graphiql-container .history-contents p {
      border: none;
    }

    .graphiql-container .historyPaneWrap {
      background: #21262b;
    }

    .graphiql-container .execute-options > li.selected,
    .graphiql-container .toolbar-menu-items > li.hover,
    .graphiql-container .toolbar-menu-items > li:active,
    .graphiql-container .toolbar-menu-items > li:hover,
    .graphiql-container .toolbar-select-options > li.hover,
    .graphiql-container .toolbar-select-options > li:active,
    .graphiql-container .toolbar-select-options > li:hover,
    .graphiql-container .history-contents > li:hover,
    .graphiql-container .history-contents > li:active {
        background: rgb(92,60,204);
        background: linear-gradient(90deg, rgba(92,60,204,1) 0%, rgba(16,193,198,1) 100%);
        color: #f0f0f0;
    }

    .graphiql-container .doc-category-title {
      border-bottom: 1px solid #181a1f;
      color: #cacdd3;
    }

    .graphiql-container .field-name {
      color: #9ca3ac;
    }

    .graphiql-container .type-name {
      color: #95be76;
    }

    .cm-property {
      color: #a5acb8;
    }

    .cm-string {
      color: #97be7b;
    }

    .cm-variable {
      color: #a87f5b;
    }

    .cm-attribute {
      color: #b58860;
    }

    .cm-def {
      color: #cc3932;
    }

    .cm-keyword {
      color: #7cf3ff;
    }

    .graphiql-container .keyword {
      color: #9ea5b0;
    }

    .graphiql-container .arg-name {
      color: #b5875d;
    }

    .graphiql-container .doc-category-item {
      color: #bc6069;
    }

    a {
      color: #7b9ad4;
    }

    .CodeMirror-lint-tooltip {
      background: #1a1e22 !important;
      color: #dfdfdf !important;
    }

    .cm-atom {
      color: #d27caf;
    }

    .CodeMirror-hints {
      background: #21262a;
      box-shadow: 0 16px 13px -10px rgba(0, 0, 0, 0.3);
    }
    .CodeMirror-hint {
      border-top: solid 1px #212629;
      color: #8ab16f;
    }
    .CodeMirror-hint-information {
      border-top: solid 1px #181a1e;
    }
    li.CodeMirror-hint-active {
      background-color: #262c2f;
      border-top-color: #212629;
      color: #b8ff87;
    }
    .CodeMirror-hint-information .content {
      color: #a4abb7;
    }

    </style>
</head>

<body>
    <div id="graphiql"></div>
    <script>
        var fetchURL = window.location.href;

        function httpUrlToWebSockeUrl(url) {
            return url.replace(/(http)(s)?\:\/\//, "ws$2://");
        }

        function graphQLFetcher(graphQLParams) {
            var headers = {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            };

            var csrfToken = Cookies.get('csrftoken');
            if (csrfToken) {
              headers['x-csrftoken'] = csrfToken;
            }

            return fetch(fetchURL, {
                method: 'post',
                headers: headers,
                body: JSON.stringify(graphQLParams),
            })
                .then(function (response) {
                    return response.text();
                })
                .then(function (responseBody) {
                    try {
                        return JSON.parse(responseBody);
                    } catch (error) {
                        return responseBody;
                    }
                });
        }

        var subscriptionsEndpoint = httpUrlToWebSockeUrl(fetchURL);
        var subscriptionsEnabled = JSON.parse('true')

        const subscriptionsClient =
            subscriptionsEnabled ? new window.SubscriptionsTransportWs.SubscriptionClient(
                subscriptionsEndpoint,
                {
                    reconnect: true
                }
            ) : null;

        const graphQLFetcherWithSubscriptions =
            window.GraphiQLSubscriptionsFetcher.graphQLFetcher(
                subscriptionsClient,
                graphQLFetcher
            );

        ReactDOM.render(
            React.createElement(GraphiQLWithExtensions.GraphiQLWithExtensions, {
                fetcher: graphQLFetcherWithSubscriptions,
            }),
            document.getElementById('graphiql'),
        );
    </script>
</body>

</html>
""".strip()  # noqa: B950