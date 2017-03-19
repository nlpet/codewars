extension String {
    var first: String {
        return String(characters.prefix(1))
    }
    var last: String {
        return String(characters.suffix(1))
    }
    var uppercaseFirst: String {
        return first.uppercased() + String(characters.dropFirst())
    }
}

func accum(_ s: String) -> String {
  var result: [String] = []
  let lcs = s.lowercased()
  for (ix, ch) in lcs.characters.enumerated() {
    let str = String(repeating: String(ch), count: ix + 1).uppercaseFirst
    result.append(str)
  }
  return result.joined(separator: "-")
}


print(accum("abc"))
print(accum("zxfupfe"))
print(accum("rqaezty"))
