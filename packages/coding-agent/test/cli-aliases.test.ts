import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";

const packageJsonPath = join(dirname(fileURLToPath(import.meta.url)), "..", "package.json");

describe("CLI aliases", () => {
	it("points every brand alias at the same binary as dek-agent", () => {
		const manifest = JSON.parse(readFileSync(packageJsonPath, "utf8")) as {
			bin?: Record<string, string>;
			piConfig?: { name?: string };
		};
		const target = manifest.bin?.["dek-agent"];
		expect(target).toBeTruthy();
		// Each rebrand adds an alias rather than renaming one, so every past
		// name has to keep resolving. REBRAND_MIGRATION.md keeps dek-agent as
		// the documented default.
		for (const alias of ["pi", "spider-agent", "copider-code"]) {
			expect(manifest.bin?.[alias]).toBe(target);
		}
	});

	it("tracks the current brand in piConfig.name without moving the env contract", async () => {
		const manifest = JSON.parse(readFileSync(packageJsonPath, "utf8")) as {
			piConfig?: { name?: string };
		};
		expect(manifest.piConfig?.name).toBe("copider-code");

		// piConfig.name drives display only. Deriving the env prefix from it
		// renamed PRIME_AGENT_* out from under users on every rebrand.
		const { ENV_SESSION_DIR, ENV_AGENT_DIR } = await import("../src/config.js");
		expect(ENV_SESSION_DIR).toBe("PRIME_AGENT_SESSION_DIR");
		expect(ENV_AGENT_DIR).toBe("PRIME_AGENT_CODING_AGENT_DIR");
	});
});
