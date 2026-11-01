import { useEffect, useState } from "react";

function NewsAggregator() {
  const [news, setNews] = useState([]);
  const [search, setSearch] = useState("");
  const [sourceFilter, setSourceFilter] = useState("all");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchNews();
  }, []);

  const fetchNews = async () => {
    setLoading(true);
    setError(null);

    try {
      // Check cache first
      const cachedNews = localStorage.getItem("cachedNews");
      const cachedTime = localStorage.getItem("cachedNewsTime");

      const fiveMinutes = 5 * 60 * 1000;

      if (
        cachedNews &&
        cachedTime &&
        Date.now() - Number(cachedTime) < fiveMinutes
      ) {
        setNews(JSON.parse(cachedNews));
        setLoading(false);
        return;
      }

      // Fetch both APIs at the same time
      const [hnResponse, spaceResponse] = await Promise.all([
        fetch(
          "https://hn.algolia.com/api/v1/search_by_date?tags=story&hitsPerPage=15"
        ),
        fetch(
          "https://api.spaceflightnewsapi.net/v4/articles/?limit=15"
        ),
      ]);

      if (!hnResponse.ok || !spaceResponse.ok) {
        throw new Error("Failed to fetch news");
      }

      const hnData = await hnResponse.json();
      const spaceData = await spaceResponse.json();

      // Convert Hacker News data into our standard format
      const hackerNews = hnData.hits.map((item) => ({
        id: `hn-${item.objectID}`,
        title: item.title || "No title",
        description: `By ${item.author}`,
        url: item.url || `https://news.ycombinator.com/item?id=${item.objectID}`,
        source: "Hacker News",
        publishedAt: item.created_at,
      }));

      // Convert Spaceflight News data into our standard format
      const spaceNews = spaceData.results.map((item) => ({
        id: `space-${item.id}`,
        title: item.title,
        description: item.summary || "No description",
        url: item.url,
        source: "Spaceflight News",
        publishedAt: item.published_at,
      }));

      // Combine both arrays
      const combinedNews = [...hackerNews, ...spaceNews];

      setNews(combinedNews);

      // Save to cache
      localStorage.setItem(
        "cachedNews",
        JSON.stringify(combinedNews)
      );

      localStorage.setItem(
        "cachedNewsTime",
        Date.now().toString()
      );
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const filteredNews = news.filter((item) => {
    const matchesSearch =
      item.title.toLowerCase().includes(search.toLowerCase()) ||
      item.description.toLowerCase().includes(search.toLowerCase());

    const matchesSource =
      sourceFilter === "all" ||
      item.source === sourceFilter;

    return matchesSearch && matchesSource;
  });

  if (loading) {
    return <h2>Loading news...</h2>;
  }

  if (error) {
    return (
      <div>
        <h2>Error: {error}</h2>
        <button onClick={fetchNews}>Try Again</button>
      </div>
    );
  }

  return (
    <div className="container">
      <h1>News Aggregator</h1>

      <div className="controls">
        <input
          type="text"
          placeholder="Search news..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <select
          value={sourceFilter}
          onChange={(e) => setSourceFilter(e.target.value)}
        >
          <option value="all">All Sources</option>
          <option value="Hacker News">
            Hacker News
          </option>
          <option value="Spaceflight News">
            Spaceflight News
          </option>
        </select>

        <button onClick={fetchNews}>
          Refresh
        </button>
      </div>

      <p>
        Showing {filteredNews.length} articles
      </p>

      <div className="news-grid">
        {filteredNews.map((item) => (
          <div key={item.id} className="news-card">
            <h2>{item.title}</h2>

            <p>{item.description}</p>

            <p>
              <strong>Source:</strong>{" "}
              {item.source}
            </p>

            <p>
              {new Date(
                item.publishedAt
              ).toLocaleString()}
            </p>

            <a
              href={item.url}
              target="_blank"
              rel="noreferrer"
            >
              Read Article
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default NewsAggregator;