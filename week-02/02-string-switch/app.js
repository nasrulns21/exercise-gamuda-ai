export function actionFromString(value) {
  if (typeof value !== 'string') return 'Unknown action'
  switch (value.trim().toLowerCase()) {
    case 'start': return 'System started'
    case 'pause': return 'System paused'
    case 'stop': return 'System stopped'
    default: return 'Unknown action'
  }
}
