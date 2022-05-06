class Solution:
	def restoreIpAddresses(self, s: str) -> List[str]:

		def valid(section):
			return (section[0] != "0" and int(section) <= 255) or len(section) == 1

		def find_ips(index, ip, ip_sections):
			if index == len(s) and ip_sections == 0:
				result.append(ip)
				return
			if ip_sections > 0:
				word = ""
				while index < len(s):
					word += s[index]
					if valid(word): find_ips(index+1, ip + word + "." if ip_sections > 1 else ip + word, ip_sections-1)
					index += 1

		result = []
		find_ips(0,"",4)
		return result
