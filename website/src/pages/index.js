import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          Physical AI Specification Kit
        </Heading>
        <p className="hero__subtitle">A comprehensive resource for understanding and developing Physical AI systems</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/chat">
            Start Chatting with the Knowledge Base
          </Link>
        </div>
      </div>
    </header>
  );
}

function FeatureSection() {
  return (
    <section className={clsx(styles.section, styles.features)}>
      <div className="container">
        <div className="row">
          <div className="col col--4">
            <div className="text--center padding-horiz--md">
              <h3>Physical AI Defined</h3>
              <p>
                Physical AI represents a fundamental shift from traditional software-based artificial intelligence toward systems that exist, operate, and learn within the physical world. Unlike conventional AI that processes data in virtual environments, Physical AI systems are embodied—they possess physical form and directly interact with the tangible world through sensors and actuators.
              </p>
            </div>
          </div>
          <div className="col col--4">
            <div className="text--center padding-horiz--md">
              <h3>Embodied Intelligence</h3>
              <p>
                The essence of Physical AI lies in the integration of intelligence with physicality. These systems must navigate the complexities of real-world physics, handle uncertainty inherent in physical interactions, and operate under real-time constraints while maintaining safety for both the system and its environment.
              </p>
            </div>
          </div>
          <div className="col col--4">
            <div className="text--center padding-horiz--md">
              <h3>Real-World Applications</h3>
              <p>
                From manufacturing and healthcare to exploration and service industries, Physical AI systems bridge the gap between virtual AI capabilities and real-world application, addressing challenges that require systems capable of operating effectively in the physical world.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function ContentSection() {
  return (
    <section className={styles.section}>
      <div className="container">
        <div className="row">
          <div className="col col--8 col--offset-2">
            <h2>Understanding Physical AI</h2>
            <p>
              Physical AI fundamentally differs from software-based AI systems in several key aspects:
            </p>
            <ul>
              <li><strong>Embodiment and Real-World Presence:</strong> Physical AI systems have mass, occupy space, and must comply with the laws of physics. This embodiment is integral to how these systems perceive, reason, and act.</li>
              <li><strong>Continuous Interaction and Real-Time Constraints:</strong> Unlike software-based systems that can pause computation, Physical AI systems must operate continuously within real-time constraints.</li>
              <li><strong>Safety and Physical Consequences:</strong> Physical AI systems must account for the real-world consequences of their actions, fundamentally changing the approach to system design and validation.</li>
              <li><strong>Sensorimotor Integration:</strong> These systems must tightly integrate perception and action in continuous loops, creating feedback mechanisms fundamental to their operation and learning.</li>
            </ul>
            <p>
              This specification kit provides a comprehensive framework for understanding how Physical AI systems differ from their software-based counterparts and how these differences shape the design, implementation, and application of embodied intelligence systems.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title} - Physical AI Specification Kit`}
      description="A comprehensive resource for understanding and developing Physical AI systems">
      <HomepageHeader />
      <main>
        <FeatureSection />
        <ContentSection />
      </main>
    </Layout>
  );
}
