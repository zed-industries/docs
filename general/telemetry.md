# Telemetry in Zed

Zed collects anonymous telemetry data to help the team understand how people are using the app. When we release the public beta, we'll provide the ability to opt out of telemetry, but during the alpha, it isn't configurable.

The telemetry data is not shared with Zed's servers, but is sent directly to an analytics service called [Mixpanel](https://mixpanel.com), where it remains anonymous, and can't be related to specific Zed users. Events are reported over HTTPS, and requests are rate-limited to avoid using significant network bandwidth.

Currently, the events that are reported are:

-   Opening the app
-   Signing in
-   Opening and saving files. File extensions (e.g. `.rs`, `.html`, `.txt`) are included in these events.

All events also include your OS version, Zed app version, and a timestamp.

## Auditing your Telemetry Events

You can see the telemetry data that Zed has reported by running the command `zed: open telemetry log` from the command palette, or clicking `Help > View Telemetry Log` in the application menu.

If you have concerns about telemetry, please feel free to open issues in our [community repository](https://github.com/zed-industries/community/issues/new/choose).
