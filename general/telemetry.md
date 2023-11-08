# Telemetry in Zed

**Up to date with v0.112.0**

Zed collects anonymous telemetry data to help the team understand how people are using the application and to see what sort of severe issues they are experiencing.

## Types of Telemetry

### Diagnostics

Diagnostic events include debug information (stack traces) from crash reports.  Crash reports are sent to a cloud-monitoring service called [Datadog](https://www.datadoghq.com).  Within Datadog, we can visualize how frequently users are running into issues and assess the severity of the issue.  Having these crash reports sent automatically allows us to begin implementing fixes without the user needing to file a report in our issue tracker.  Being able to see various crashes plotted in Datadog also gives us an informal measurement of the stability of Zed.

### Metrics

Zed also collects metric information based on user actions.  Metric events are reported over HTTPS, and requests are rate-limited to avoid using significant network bandwidth. Telemetry data is proxied through our servers simply to enable us to easily switch analytics services; we never store this data.  Currently, we are using [Clickhouse](https://clickhouse.com) to ingest the events.  All data remains anonymous, and can't be related to specific Zed users.

The following data is sent:

#### ClickhouseEventRequestBody

- `token`: An identifier that is used to authenticate the request on zed.dev
- `installation_id`: An identifier that is unique to each installation of Zed (this differs for stable, preview, and devs builds)
- `session_id`: An identifier that is unique to each session of Zed (this differs for each time you open Zed)
- `is_staff`: A boolean that indicates whether the user is a member of the Zed team or not
- `app_version`: Zed's app version
- `os_name`: The name of your operating system
- `os_version`: The version of your operating system
- `architecture`: The architecture of your CPU
- `release_channel`: Zed's release channel
    - `stable`
    - `preview`
    - `dev`
- `events`: A vector of `ClickhouseEventWrapper`s

#### ClickhouseEventWrapper

- `signed_in`: A boolean that indicates whether the user is signed in or not
- `event`: An enum, where each variant can be one one of the following `ClickhouseEvent` variants:

#### ClickhouseEvent

- `editor`
    - `operation`: The editor operation that was performed
        - `open`
        - `save`
    - `file_extension`: The extension of the file that was opened or saved
    - `vim_mode`: A boolean that indicates whether the user is in vim mode or not
    - `copilot_enabled`: A boolean that indicates whether the user has copilot enabled or not
    - `copilot_enabled_for_language`: A boolean that indicates whether the user has copilot enabled for the language of the file that was opened or saved
- `copilot`
    - `suggestion_id`: The ID of the suggestion
    - `suggestion_accepted`: A boolean that indicates whether the suggestion was accepted or not
    - `file_extension`: The file extension of the file that was opened or saved
- `call`
    - `operation`: The call operation that was performed
        - `accept incoming`
        - `decline incoming`
        - `disable microphone`
        - `disable screen share`
        - `enable microphone`
        - `enable screen share`
        - `hang up`
        - `invite`
        - `join channel`
        - `open channel notes`
        - `share project`
        - `unshare project`
    - `room_id`: The ID of the room
    - `channel_id`: The ID of the channel
- `assistant`
    - `conversation_id`: The ID of the conversation (for panel events only)
    - `kind`: An enum with the following variants:
        - `panel`
        - `inline`
    - `model`: The model that was used
- `cpu`
    - `usage_as_percentage`: The CPU usage
    - `core_count`: The number of cores on the CPU
- `memory`
    - `memory_in_bytes`: The amount of memory used in bytes
    - `virtual_memory_in_bytes`: The amount of virtual memory used in bytes

You can audit the metrics data that Zed has reported by running the command `zed: open telemetry log` from the command palette, or clicking `Help > View Telemetry Log` in the application menu.

## Configuring Telemetry Settings

You have full control over what data is sent out by Zed.  To enable or disable some or all telemetry types, open your `settings.json` file via `zed: open settings` from the command palette.  Insert and tweak the following:

```json
"telemetry": {
    "diagnostics": false,
    "metrics": false
},
```

The telemetry settings can also be configured via the `welcome` screen, which can be invoked via the `workspace: welcome` action in the command palette.

## Concerns and Questions

If you have concerns about telemetry, please feel free to open issues in our [community repository](https://github.com/zed-industries/community/issues/new/choose).
