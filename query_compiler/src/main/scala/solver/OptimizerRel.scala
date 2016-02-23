package duncecap

object OptimizerRel {
  def fromRel(rel:Rel, rule:Rule):OptimizerRel = {
    OptimizerRel(
      rel.getName(),
      rel.attrs,
      rel.anno,
      false,
      rel.getAnnotations()
        .filter(attr => rule.getFilters().selections.find(selection => selection.getAttr() == attr).isDefined).toSet)
  }

  def toRel(rel:OptimizerRel): Rel = {
    Rel(
      rel.name,
      rel.attrs,
      if (rel.anno.values.size == 1 && rel.anno.values.head == "") Annotations(List()) else rel.anno
    )
  }

  def createImaginaryOptimizerRelWithNoSelects(attrs:Iterable[String]) = {
    new OptimizerRel(
      "",
      Attributes(attrs.toList),
      Annotations(List("void*")),
      true,
      attrs.toSet)
  }
}

/**
 * The class that replaces QueryRelation
 * @param name
 * @param attrs
 * @param anno
 * @param isImaginary
 * @param nonSelectedAttrNames
 */
case class OptimizerRel(override val name:String,
                   override val attrs:Attributes,
                   override val anno:Annotations,
                   val isImaginary:Boolean,
                   val nonSelectedAttrNames:Set[String]) extends RelBase