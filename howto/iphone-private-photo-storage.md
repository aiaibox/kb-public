---
id: 01M1TTPR4EYXQH418D9SPG8DKH
title: "Storing a photo privately on iPhone"
repo: public
tags: [reference, security]
created: 2026-09-06
updated: 2026-09-06
---

# Storing a photo privately on iPhone

**Scope:** Keeping a photo off casual view on an iPhone, and which messaging
apps render a chat wallpaper only on your own device. Does not cover cloud or
backup privacy, threat models involving device seizure, or Android.

## Conclusion

**Do not use a chat background as private storage.** iMessage Conversation
Backgrounds (iOS 18) are **shared with both participants** — Messages offers no
background visible only to you. Even in apps where the wallpaper is device-local,
the chat list, app switcher and notification previews can surface it.

Store the photo instead:

1. **Photos → Hidden album.** Select the photo → ⋯ → Hide. Then
   *Settings → Photos*: enable **Use Face ID** and disable **Show Hidden Album**.
   The album then disappears from the Albums list and opens only after Face ID.
2. **Locked Note** (more covert). Put the photo in a Note → ⋯ → **Lock with
   Face ID**, and give the note a dull name. This keeps it out of the Photos
   library entirely.

If a per-chat wallpaper is genuinely wanted, **WhatsApp** is the one to use: its
wallpaper is device-local and never synced to the other party.

## Verify

```
Settings → Photos: 'Use Face ID' on, 'Show Hidden Album' off.
  The Hidden album should vanish from Photos → Albums and require Face ID.
iMessage: set a Conversation Background, then check the other participant's
  device — it appears there too, proving it is shared rather than local.
```

## Messaging apps compared

| App | Per-chat wallpaper | Notes |
|---|---|---|
| WhatsApp | device-local | not synced to the contact — the safe choice |
| Telegram | device-local | widest theme and background customisation |
| Signal | device-local | strongest privacy posture overall |
| Messenger | chat themes | supported |
| iMessage | **shared** | iOS 18 Conversation Backgrounds apply to both parties |
| WeChat | none | no personal chat background setting |

## Rejected

| Option | Reason |
|---|---|
| iMessage Conversation Background | Shared with both parties by design |
| Contact photo / Contact Poster | Shows on incoming calls and in message lists |
| Any chat background for a sensitive image | Chat list, app switcher and notification previews can expose it |
| Third-party vault apps | Require trusting a third-party developer, and often carry ads or subscriptions; the built-in Hidden album needs no extra trust |

## Open

- Feature availability varies by iOS version — Conversation Backgrounds exist
  only on iOS 18 and later. Verify on the device rather than assuming.

## References

- https://www.apple.com/ios/ — Hidden album, locked Notes, Conversation Backgrounds
- https://www.whatsapp.com — device-local per-chat wallpaper
- https://telegram.org — background customisation
- https://signal.org — privacy-focused alternative
