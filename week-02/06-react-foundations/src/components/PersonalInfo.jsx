import './PersonalInfo.css'

export default function PersonalInfo({ now = new Date() }) {
  const date = new Intl.DateTimeFormat('en-GB', {day:'numeric',month:'long',year:'numeric',timeZone:'Asia/Kuala_Lumpur'}).format(now)
  const time = new Intl.DateTimeFormat('en-GB', {hour:'2-digit',minute:'2-digit',hour12:false,timeZone:'Asia/Kuala_Lumpur'}).format(now)
  return <section className="profile" aria-labelledby="profile-name">
    <h1>Personal Information</h1>
    <img src="./profile.png" alt="Nasrul Sharuddin profile"/>
    <h2 id="profile-name">Nasrul Sharuddin</h2>
    <dl><div><dt>Email</dt><dd>nasrul@example.com</dd></div><div><dt>Age</dt><dd>34</dd></div></dl>
    <h3>Hobbies</h3><ul><li>Reading</li><li>Photography</li><li>Learning AI</li></ul>
    <p className="clock"><strong>Current date and time</strong><span>{date} · {time}</span></p>
  </section>
}
