# Telemetry in Zed

Zed collects anonymous telemetry data to help the team understand how people are using the application and to see what sort of severe issues they are experiencing.

## Types of Telemetry

### Diagnostics

Diagnostic events include debug information (stack traces) from crash reports.  Crash reports are sent to a cloud-monitoring service called [Datadog](https://www.datadoghq.com).  Within Datadog, we can visualize how frequently users are running into issues and assess the severity of the issue.  Having these crash reports sent automatically allows us to begin implementing fixes without the user needing to file a report in our issue tracker.  Being able to see various crashes plotted in Datadog also gives us an informal measurement of the stability of Zed.

### Metrics

Zed also collects metric information based on user actions.  Metric events are reported over HTTPS, and requests are rate-limited to avoid using significant network bandwidth. The telemetry data is not shared with Zed's servers; it is sent directly to an analytics service called [Mixpanel](https://mixpanel.com), where it remains anonymous, and can't be related to specific Zed users.

The following actions are captured:

- Opening the app
- Signing in
- Opening and saving files. File extensions (e.g. `.rs`, `.html`, `.txt`) are included in these events; code is *never* included in these events.

All `metrics` events also include your OS version, Zed app version, and a timestamp.

You can audit the metrics data that Zed has reported by running the command `zed: open telemetry log` from the command palette, or clicking `Help > View Telemetry Log` in the application menu.

## Configuring Telemetry Settings

You have full control over what data is sent out by Zed.  To enable or disable some or all telemetry types, open your `settings.json` file via `zed: open settings` from the command palette.  Insert and tweak the following:

```json
"telemetry": {
    "diagnostics": true,
    "metrics": false
},
```

## Concerns and Questions

If you have concerns about telemetry, please feel free to open issues in our [community repository](https://github.com/zed-industries/community/issues/new/choose).
